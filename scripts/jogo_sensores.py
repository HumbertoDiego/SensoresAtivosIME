"""Jogo para Jupyter. Uso: from jogo_sensores import jogar; jogar()."""
import html
import json
import warnings

CARTOES = [
    ('Opera no visível e/ou infravermelho refletido', 'optico'),
    ('Registra a radiação solar refletida pelos alvos', 'optico'),
    ('Depende de uma fonte externa de iluminação', 'optico'),
    ('É um sensor passivo', 'optico'),
    ('Depende da iluminação solar para observar a superfície', 'optico'),
    ('Nuvens podem impedir a observação da superfície', 'optico'),
    ('Ruído aditivo: modelo simplificado Z = X + Y', 'optico'),
    ('Opera na faixa de micro-ondas', 'radar'),
    ('Emite energia e mede o sinal retroespalhado pelos alvos', 'radar'),
    ('Possui sua própria fonte de iluminação', 'radar'),
    ('É um sensor ativo', 'radar'),
    ('Pode operar de dia ou à noite', 'radar'),
    ('Geralmente atravessa nuvens; a chuva pode atenuar o sinal', 'radar'),
    ('Speckle: modelo multiplicativo simplificado Z = X x Y', 'radar'),
]


def jogar(altura=680, cartoes=None):
    """Exibe uma nova partida independente no notebook.

    altura: altura do quadro em pixels (padrão: 680).
    cartoes: lista opcional de pares (texto, 'optico' ou 'radar').
    Arraste, ou selecione um cartão e clique na coluna de destino.
    Para teclado: Enter no cartão e Enter na área de destino.
    Não exige conexão à internet nem extensões de widgets.
    """
    from IPython.display import HTML, display, IFrame
    if isinstance(altura, bool) or not isinstance(altura, int) or altura < 300:
        raise ValueError('altura deve ser um inteiro de pelo menos 300 pixels.')
    itens = list(CARTOES if cartoes is None else cartoes)
    if not itens or any(len(i) != 2 or not isinstance(i[0], str)
                        or i[1] not in ('optico', 'radar') for i in itens):
        raise ValueError('Use pares (texto, "optico" ou "radar").')
    dados = json.dumps(itens, ensure_ascii=False).replace('<', '\\u003c')
    pagina = _PAGINA.replace('__DADOS__', dados)
    with warnings.catch_warnings():
        warnings.filterwarnings(
            "ignore",
            message=r"Consider using IPython\.display\.IFrame instead",
            category=UserWarning,
        )
        display(HTML(
            '<iframe title="Jogo: óptico ou radar" sandbox="allow-scripts" '
            f'style="width:100%;height:{altura}px;border:0;" '
            f'srcdoc="{html.escape(pagina, quote=True)}"></iframe>'
        ))

_PAGINA = r'''<!doctype html><html lang="pt-BR"><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>
*{box-sizing:border-box}body{margin:0;padding:12px;background:#f3f6fb;color:#17304c;font:14px system-ui,sans-serif}
h1{font-size:22px;margin:0 0 5px}p{margin:6px 0 10px}.intro{color:#52647a}
.panel{background:white;border:1px solid #ccd9e8;border-radius:10px;overflow:hidden}
h2{font-size:15px;margin:0;padding:9px 12px;background:#e6eef8}
.columns{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:12px 0}
.zone{padding:8px;min-height:100px;display:grid;grid-template-columns:1fr 1fr;align-content:start;gap:7px}
.bank .zone{grid-template-columns:repeat(4,minmax(0,1fr));min-height:50px}
.columns .zone{max-height:270px;overflow-y:auto}
.zone:empty:after{content:attr(data-empty);color:#76879a;padding:20px 5px;grid-column:1/-1;text-align:center}
.zone.over{background:#e0efff}.card{font:inherit;font-size:12px;line-height:1.3;text-align:left;background:white;color:#20344b;border:1px solid #cbd7e5;border-radius:7px;padding:8px;cursor:grab;overflow-wrap:anywhere}
.card:hover{border-color:#2774c5}.card.selected{outline:2px solid #2774c5;background:#edf5ff}
.card.correct{border:2px solid #278451;background:#ecf9f0}.card.wrong{border:2px solid #c64a4a;background:#fff0f0}
.feedback{display:block;font-size:11px;font-weight:bold;margin-top:4px}
button:focus-visible,.zone:focus-visible{outline:3px solid #3984dc;outline-offset:2px}
.actions{display:flex;gap:8px}.actions button{border:0;border-radius:8px;padding:9px 13px;font:inherit;font-weight:600;cursor:pointer;background:#e0e8f2;color:#17304c}.actions .primary{background:#1559a2;color:white}
#status{font-weight:600;min-height:20px}.note{font-size:11px;color:#66788c}
@media(max-width:600px){.bank .zone{grid-template-columns:repeat(2,minmax(0,1fr))}.columns .zone{grid-template-columns:1fr}}
</style>
<h1>Óptico ou radar?</h1><p class="intro">Arraste os cartões ou clique no cartão e depois na coluna.</p>
<section class="panel bank"><h2>Características disponíveis</h2><div id="banco" class="zone" tabindex="0" aria-label="Características disponíveis" data-empty="Todos os cartões foram distribuídos."></div></section>
<div class="columns">
<section class="panel"><h2>☀ Sensor óptico passivo</h2><div id="optico" class="zone" tabindex="0" aria-label="Coluna óptico" data-empty="Solte aqui"></div></section>
<section class="panel"><h2>📡 Sensor de radar ativo</h2><div id="radar" class="zone" tabindex="0" aria-label="Coluna radar" data-empty="Solte aqui"></div></section></div>
<div class="actions"><button id="verificar" class="primary">Verificar respostas</button><button id="reiniciar">Recomeçar e embaralhar</button></div>
<p id="status" role="status" aria-live="polite"></p>

<script>
const dados=__DADOS__, zonas=[...document.querySelectorAll('.zone')], status=document.getElementById('status');
let selecionado=null,arrastando=null;
function limpar(){document.querySelectorAll('.card').forEach(c=>{c.classList.remove('correct','wrong');c.querySelector('.feedback')?.remove()});status.textContent=''}
function selecionar(c){document.querySelectorAll('.selected').forEach(x=>x.classList.remove('selected'));selecionado=selecionado===c?null:c;if(selecionado)selecionado.classList.add('selected')}
function mover(c,z){if(!c)return;limpar();z.appendChild(c);c.classList.remove('selected');selecionado=null;arrastando=null}
zonas.forEach(z=>{
z.addEventListener('dragover',e=>{e.preventDefault();e.dataTransfer.dropEffect='move';z.classList.add('over')});
z.addEventListener('dragleave',e=>{if(!z.contains(e.relatedTarget))z.classList.remove('over')});
z.addEventListener('drop',e=>{e.preventDefault();z.classList.remove('over');mover(arrastando,z)});
z.addEventListener('click',e=>{if(!e.target.closest('.card'))mover(selecionado,z)});
z.addEventListener('keydown',e=>{if(e.target===z&&(e.key==='Enter'||e.key===' ')){e.preventDefault();mover(selecionado,z)}});
});
function iniciar(){selecionado=null;arrastando=null;zonas.forEach(z=>{z.replaceChildren();z.classList.remove('over')});const ids=dados.map((_,i)=>i);for(let i=ids.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[ids[i],ids[j]]=[ids[j],ids[i]]}
ids.forEach(i=>{const c=document.createElement('button');c.type='button';c.className='card';c.draggable=true;c.dataset.indice=i;c.textContent=dados[i][0];c.addEventListener('click',e=>{e.stopPropagation();selecionar(c)});c.addEventListener('dragstart',e=>{arrastando=c;e.dataTransfer.setData('text/plain',String(i));e.dataTransfer.effectAllowed='move'});c.addEventListener('dragend',()=>{arrastando=null;zonas.forEach(z=>z.classList.remove('over'))});document.getElementById('banco').appendChild(c)});status.textContent='Distribua os '+dados.length+' cartões.'}
document.getElementById('verificar').onclick=()=>{limpar();let acertos=0,n=0;document.querySelectorAll('.card').forEach(c=>{const col=c.parentElement.id;if(col==='banco')return;n++;const certo=col===dados[Number(c.dataset.indice)][1];if(certo)acertos++;c.classList.add(certo?'correct':'wrong');const f=document.createElement('span');f.className='feedback';f.textContent=certo?'✓ Correto':'↔ Tente outra coluna';c.appendChild(f)});status.textContent=acertos===dados.length?'🎉 Parabéns! Todos corretos!':`${acertos} de ${dados.length} corretos. ${dados.length-n} ainda não classificados. Você pode tentar novamente.`};
document.getElementById('reiniciar').onclick=iniciar;iniciar();
</script></html>'''

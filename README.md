# Sensores Ativos — IME

Aulas de Sensores Ativos (RADAR e LiDAR) para o 5º ano do Curso de Engenharia Cartográfica do Instituto Militar de Engenharia.

**Maj Diego · 1º semestre de 2027**

ORIGEM DA DISCIPLINA

- Projeto Radiografia da Amazônia (2007/2008): um olhar para os sensores ativos [ineficácia óptica];
- Quebra de paradigma (DSG): produção x recursos humanos e tecnológicos;
- Suporte a pesquisas envolvendo busca de soluções para o mapeamento amazônico.

NECESSIDADE DE ALTERAÇÕES
- Ensino por competências: caráter menos eletrônico, mais cartográfico/ambiental [aplicado];
- Tendências na Geoinformação: acréscimo de tópicos referentes a LiDAR; avanço das IA's;

![Plano do semestre](media/imgs/Sensores%20Ativos.png)

## Sumário

| Aula | Notebook | Conteúdo |
| --- | --- | --- |
| 1 | [Visão geral sobre RADAR e LiDAR](01_introdu%C3%A7%C3%A3o.ipynb) | Qualidades e limitações do sensoriamento ativo; Conceituar RAR; Descrever a geometria RAR; Conceituar SAR; Descrever a geometria SAR; Conceituar LiDAR. |
| 2 | [Processamento SAR I — resolução e formação da imagem](02_processamento_sar.ipynb) | Distinguir resolução espacial e amostragem; Explicar compressão de pulso e focalização SAR; Relacionar algoritmos de formação e qualidade da imagem. |
| 3 | [Processamento SAR II — produtos, calibração e multilook](03_processamento_multilook.ipynb) | Interpretar produtos e planejar o processamento; Explicar calibração radiométrica e correção geométrica; Analisar multilook e o compromisso entre variância e detalhe. |
| 4 | [Ruído speckle — estatística e filtragem](04_ruido_speckle.ipynb) | Explicar a origem física e o modelo estatístico do speckle; Comparar filtros espaciais e adaptativos; Avaliar homogeneidade, bordas e adequação à aplicação. |
| 5 | [Classificação SAR — treinamento, validação e inferência](05_classificacao_sar.ipynb) | Definir classes e atributos SAR; Separar treinamento, validação e teste sem vazamento; Interpretar métricas e executar inferência. |
| 6 | [PolSAR e InSAR — polarização, fase e relevo](06_polsar_insar.ipynb) | Explicar polarimetria e mecanismos de espalhamento; Relacionar fase interferométrica e geometria; Descrever processamento InSAR e geração de MDT. |
| 7 | [LiDAR I — aquisição, georreferenciamento e aplicações](07_lidar.ipynb) | Descrever aquisição LiDAR e retornos; Explicar georreferenciamento e fontes de incerteza; Relacionar aplicações, produtos e controle de qualidade. |
| 8 | [LiDAR II — pré-processamento e descritores de forma](08_preprocessamento_lidar.ipynb) | Analisar vizinhanças e remover pontos espúrios com SOR; Explicar CSF e classificação de terreno; Aplicar voxelização e downsampling com escala explícita; Derivar descritores geométricos locais. |
| 9 | [Registro I — referenciais, transformações e pontos homólogos](09_transformacoes_registro.ipynb) | Distinguir mudança de referencial e registro geométrico; Compor e inverter transformações entre espaços; Estimar transformação rígida por pontos homólogos. |
| 10 | [Registro II — Iterative Closest Point e validação](10_icp.ipynb) | Explicar o ciclo de otimização ICP; Comparar funções objetivo e estratégias robustas; Validar registro e preparar a prática. |
| 11 | [Classificação LiDAR — atributos, modelos e avaliação](11_classificacao_lidar.ipynb) | Construir atributos e uma legenda semântica; Comparar modelos e organizar treinamento e inferência; Avaliar classes e discutir limitações cartográficas. |

## Ferramentas para as práticas

As ferramentas abaixo apoiam atividades futuras; não são requisitos para ler as aulas. A instalação deve acompanhar o ambiente e a atividade proposta.

- Google Colab, Python e Jupyter.
- VS Code e extensão Jupyter.
- ESA SNAP: processamento de produtos SAR.
- GDAL: dados raster, vetoriais e sistemas de referência.
- CloudCompare: inspeção e processamento de nuvens.
- laspy: leitura e escrita LAS/LAZ; Open3D: geometria e registro; scikit-learn: classificação e métricas; PyTorch: modelos de aprendizado profundo.

## DICAS PARA GERENCIAR MÚLTIPLAS VERSÕES PYTHON:

- Instale o [Python Install Manager](https://www.python.org/downloads/)
```powershell
> py install 3.9 3.10 3.11 3.12 3.14 # Instala as versões python de 3.9 a 3.14
> python --version # Python 3.14.5
> $Env:PYTHON_MANAGER_DEFAULT = "3.12" # Altera a versão para esta seção de terminal apenas
> python --version # Python 3.12.10 --> Daqui pode-se criar o ambiente
```
- Após criar o ambiente, verifique se está usando uma cópia do Python 3.12 da pasta `.venv`:
```powershell
> python -c "import sys; print(sys.executable)" # C:\Users\...\Python\pythoncore-3.12-64\python.exe
> python -m venv .venv
> .\.venv\Scripts\Activate.ps1 
(.venv) > python -c "import sys; print(sys.executable)" # ...\cdg-ime\.venv\Scripts\python.exe
```

CRIAR O AMBIENTE:

```powershell
> python -m venv .venv
> .\.venv\Scripts\Activate.ps1 
(.venv) > python -m pip install --upgrade pip
(.venv) > python -m pip install -r requirements.txt
```

SELECIONAR O KERNEL NO VS CODE:

- `Select Kernel` > `Python Environments...` > `.venv\Scripts\python.exe`

## Referências

- ISO/TS 19130-2:2014, *Geographic information — Imagery sensor models for geopositioning — Part 2: SAR, InSAR, lidar and sonar*.
- NASA/SERVIR (2019), *The SAR Handbook*, cap. 2.
- NASA ARSET (2020), *SAR, parte 1*.
- NASA/JPL, *SAR Polarimetry*.
- scikit-learn, *Metrics and scoring*.
- Open3D, *Point cloud outlier removal*.
- Zhang et al. (2016), *An Easy-to-Use Airborne LiDAR Data Filtering Method Based on Cloth Simulation*, Remote Sensing, 8(6), 501 (DOI: 10.3390/rs8060501).
- Open3D, *ICP registration*.
- Weinmann et al. (2017), *Geometric features and their relevance for 3D point cloud classification* (DOI: 10.5194/isprs-annals-IV-1-W1-157-2017).
- Umeyama (1991), *Least-Squares Estimation of Transformation Parameters Between Two Point Patterns*, IEEE TPAMI, 13(4), 376–380 (DOI: 10.1109/34.88573).
- ESA, *Introduction to a SAR System*.

<!--
git pull sa main
git add * ; git commit -m "aula update"; git push ajustamento main
jupyter nbconvert --to slides 05_mmq_weighted.ipynb --TagRemovePreprocessor.remove_input_tags="hide_input" --SlidesExporter.reveal_scroll=True --post serve

reset
git init
git remote add sa https://github.com/HumbertoDiego/SensoresAtivosIME; git branch --set-upstream-to=sa/main 
git add * ; git commit -m "aula update"; git push sa main --force
-->


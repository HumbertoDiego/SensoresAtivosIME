# Sensores Ativos — IME

Aulas de Sensores Ativos (RADAR e LiDAR) para o 5º ano do Curso de Engenharia Cartográfica do Instituto Militar de Engenharia.

**Maj Diego · 1º semestre de 2027**

O curso aborda aquisição, geometria, processamento e interpretação de dados ativos, com ênfase em produtos cartográficos e controle de qualidade. Os 11 notebooks seguem a sequência do plano abaixo.

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

## Organização e avaliações

- Aulas 1–5: fundamentos, processamento e classificação SAR.
- **1ª VE prática:** classificação SAR, com treinamento, validação, teste, métricas e inferência, conforme a aula 5.
- Aula 6: PolSAR e InSAR, fase, relevo e aplicações.
- Aulas 7–8: LiDAR, pré-processamento e descritores de forma.
- Aulas 9–10: registro, transformações entre espaços, pontos homólogos e ICP.
- **2ª VE prática:** registro e transformações entre espaços, conforme as aulas 9–10.
- Aula 11: classificação LiDAR e discussão integrada.
- **VC e VF:** indicadas no plano do semestre. Datas, pesos e enunciados serão definidos pelo docente.

A divisão dos temas que ocupam dois encontros no mapa é: processamento SAR I/II, LiDAR I/II e registro I/II. Cada notebook contém navegação para o sumário, título, autoria, objetivos, referências, problema apresentado com esquema em Markdown e LaTeX e desenvolvimento teórico com numeração correspondente aos objetivos. Os notebooks são teóricos e não exigem execução de código ou instalação de bibliotecas.

## Como estudar

Abra o notebook pelo sumário em JupyterLab ou VS Code com a extensão Jupyter. Todos os links de arquivos são relativos ao repositório. As imagens são locais e os esquemas estão escritos nas próprias células em Markdown e LaTeX. A leitura não depende de acessar o GitHub ou outros serviços externos; use um ambiente local com suporte a notebooks e renderização de LaTeX. Consulte as referências bibliográficas na própria célula e responda às verificações de aprendizagem ao final dos tópicos.

## Ferramentas para as práticas

As ferramentas abaixo apoiam atividades futuras; não são requisitos para ler as aulas. A instalação deve acompanhar o ambiente e a atividade proposta.

- Google Colab, Python e Jupyter.
- VS Code e extensão Jupyter.
- ESA SNAP: processamento de produtos SAR.
- GDAL: dados raster, vetoriais e sistemas de referência.
- CloudCompare: inspeção e processamento de nuvens.
- laspy: leitura e escrita LAS/LAZ; Open3D: geometria e registro; scikit-learn: classificação e métricas; PyTorch: modelos de aprendizado profundo.

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

A ISO/TS 19130-2:2014 fundamenta modelos físicos e metadados de geoposicionamento. Ela não é um manual completo de filtragem, classificação ou registro; nesses temas, as células indicam referências complementares. A edição de 2014 é citada por ser o exemplar consultado, sem presumir que seja a edição vigente. O PDF de consulta não integra o material distribuído e os notebooks não dependem de sua presença no diretório.

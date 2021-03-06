[![DOI](https://zenodo.org/badge/333831359.svg)](https://zenodo.org/badge/latestdoi/333831359)
[![Documentation Status](https://readthedocs.org/projects/trisbm/badge/?version=latest)](https://trisbm.readthedocs.io/en/latest/?badge=latest)
[![Python package](https://github.com/fvalle1/trisbm/actions/workflows/python-package.yml/badge.svg)](https://github.com/fvalle1/trisbm/actions/workflows/python-package.yml)
<!--[![Conda](https://github.com/fvalle1/trisbm/actions/workflows/conda.yml/badge.svg)](https://github.com/fvalle1/trisbm/actions/workflows/conda.yml)-->
[![Docker](https://github.com/fvalle1/trisbm/actions/workflows/docker.yml/badge.svg)](https://github.com/fvalle1/trisbm/actions/workflows/docker.yml)
[![conda](https://anaconda.org/conda-forge/nsbm/badges/installer/conda.svg)](https://anaconda.org/conda-forge/nsbm)
[![GPL](https://anaconda.org/conda-forge/nsbm/badges/license.svg
)](LICENSE)

# multipartite Stochastic Block Modeling

Inheriting hSBM from [https://github.com/martingerlach/hSBM_Topicmodel](https://github.com/martingerlach/hSBM_Topicmodel) extends it to tripartite networks (aka supervised topic models)

The idea is to run SBM-based topic modeling on networks given keywords on documents

![network](network.png)

# Install
## With pip
```bash
python3 -m pip install . -vv
```


## With conda/mamba

```bash
conda install -c conda-forge nsbm
```


# Example
```python
from trisbm import trisbm
import pandas as pd
import numpy as np

df = pd.DataFrame(
index = ["w{}".format(w) for w in range(1000)],
columns = ["doc{}".format(w) for w in range(250)],
data = np.random.randint(1, 100, 250000).reshape((1000, 250)))

df_key_list = [
    pd.DataFrame(
index = ["w{}".format(w) for w in range(100+ik)],
columns = ["doc{}".format(w) for w in range(250)],
data = np.random.randint(1, 5+ik, (100+ik)*250).reshape((100+ik, 250)))
    
    for ik in range(3)
]

model = trisbm()
model.make_graph_multiple_df(df, df_key_list)

model.fit(n_init=1, B_min=50, verbose=False)
```


# Run with Docker

```bash
docker run -it -u jovyan -v $PWD:/home/jovyan/work -p 8899:8888 docker.pkg.github.com/fvalle1/trisbm/trisbm:latest
```

If a *graph.xml.gz* file is found in the current dir the analysis will be performed on it.

# Tests

```bash
python3 tests/run_tests.py
```

# Documentation

[Docs](https://fvalle1.github.io/trisbm/)

[Readthedocs](https://trisbm.readthedocs.io/en/latest/index.html)

# License

See [LICENSE](LICENSE).

This work [is in part based on](https://www.gnu.org/licenses/gpl-faq.en.html#WhyDoesTheGPLPermitUsersToPublishTheirModifiedVersions) [sbmtm](https://github.com/martingerlach/hSBM_Topicmodel)

## Third party libraries

This package depends on [graph-tool](https://graph-tool.skewed.de)

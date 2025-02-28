# Snecko Brain
Analyzing Slay the Spire, using machine learning.

# Setting up the AI part

```bash
# Install conda. I'll leave that to another guide, but I used Python 3.7 / 3.8 and miniconda.
# First create a conda environment:
conda create --name snecko
conda activate snecko

# Install dependencies
conda install -c pytorch -c fastai fastai
conda install -c conda-forge jupyterlab
conda install -c conda-forge notebook

# Run jupyter, then open scratch.ipynb
jupyter notebook

# In subsequent runs, instead of creating a new environment, reactivate your old one:
conda activate snecko
```

# Setting up the Slay The Spire mod

In Steam, subscribe to these STS mods:

* ModTheSpire
* BaseMod
* Communication Mod

Run the game via the Steam UI and a menu will let you select "Play
With Mods". Enable both BaseMod and Communication Mod in the mod
configuration UI and click "Play".

This first run should actually create some config files. Edit the
config file to make `command=` define the path to your `mod.py` entry
point. Then rerun the game, again with mods enabled, and there should
be a menu option to enable the Communication Mod to connect to the AI model.

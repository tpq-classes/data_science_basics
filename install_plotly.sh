#
# install.sh
#
apt update
apt upgrade -y

# Tools & Python
apt install vim -y
apt install gcc -y
apt install htop -y
apt install screen -y
apt install python3 -y
apt install python3-dev -y
apt install pipx -y

# Paths
export PATH=$PATH:/root/.local/bin

# Python
pipx install ipython
pipx inject ipython numpy==1.26.4
pipx inject ipython pandas
pipx inject ipython openpyxl
pipx inject ipython tables
pipx inject ipython pyarrow
pipx inject ipython jupyterlab
pipx inject ipython matplotlib
pipx inject ipython seaborn
pipx inject ipython nodejs
pipx inject ipython ipywidgets
pipx inject ipython plotly==5.22.0
pipx inject ipython cufflinks
pipx inject ipython mplfinance

ln -s /root/.local/share/pipx/venvs/ipython/bin/jupyter /root/.local/bin/jupyter

jupyter labextension install jupyterlab-plotly
jupyter labextension install plotlywidget

screen

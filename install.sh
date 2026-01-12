#
# install.sh
#
apt update
apt upgrade -y

# Tools & Python
apt install vim -y
apt install gcc -y
apt install git -y
apt install wget -y
apt install curl -y
apt install htop -y
apt install screen -y
apt install python3 -y
apt install python3-dev -y
apt install pipx -y

# Paths
export PATH=$PATH:/root/.local/bin

# Python
pipx install ipython
pipx inject ipython numpy
pipx inject ipython pandas
# pipx inject ipython openpyxl
# pipx inject ipython tables
# pipx inject ipython pyarrow
pipx inject ipython jupyterlab
pipx inject ipython matplotlib
# pipx inject ipython seaborn
pipx inject ipython pyzmq

mkdir -p ~/.vim/autoload ~/.vim/bundle && curl -LSso ~/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim
git clone --recursive https://github.com/davidhalter/jedi-vim.git ~/.vim/bundle/jedi-vim
cp vimrc ~/.vimrc

ln -s /root/.local/share/pipx/venvs/ipython/bin/jupyter /root/.local/bin/jupyter
ln -s /root/.local/share/pipx/venvs/ipython/bin/python3 /root/.local/bin/python

echo "source ~/.local/share/pipx/venvs/ipython/bin/activate" > ~/.bashrc

screen

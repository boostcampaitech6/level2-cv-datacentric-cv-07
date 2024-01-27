
cd ..
echo -e "\e[34mMove to the parent directory\e[0m"

# data 다운로드
if [ -d "data" ] ; then
	echo -e "\e[34mdata directory is already exist\e[0m"
else
	wget https://aistages-api-public-prod.s3.amazonaws.com/app/Competitions/000273/data/data.tar.gz
	tar -zxvf data.tar.gz
	rm data.tar.gz
fi
echo -e "\e[34mFin data download\e[0m"

# code 다운로드
if [ -d "code" ] ; then
	echo -e "\e[34mcode directory is already exist\e[0m"
else
	wget https://aistages-api-public-prod.s3.amazonaws.com/app/Competitions/000273/data/code.tar.gz
	tar -zxvf code.tar.gz
	rm code.tar.gz
fi
echo -e "\e[34mFin code download\e[0m"

# git 설정
git config --global commit.template ./.commit_template
git config --global core.editor "code --wait"
echo -e "\e[34mFin git config\e[0m"

# pre-commit 설정
pre-commit autoiupdate
pre-commit install
echo -e "\e[34mFin pre-commit\e[0m"

# install requirements
cd code
apt install gcc
apt install g++
pip install -r requirements.txt
echo -e "\e[34mFin install requirements\e[0m"

cd ../level2-cv-datacentric-cv-07
echo -e "\e[34mFin init\e[0m"

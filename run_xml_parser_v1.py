import bs4 as bs
import sys
import glob
import csv
import os


def run_parser(indir, outdir):

	#check report type
	label1, label2, label3 = '', '', ''
	list_of_files = glob.glob(str(indir) + '/*.xml')
	for indir in list_of_files:
		input_folder = indir.split('/')[-2]
		category1, category2, category3 = '', '', ''
		log += str(indir)
		fp = open(indir).read()
		soup = bs.BeautifulSoup(fp,'xml')

		for k in soup.find_all('LABEL'):
			str_ = ''
			if label1 == k.string:
				lable2 += soup.find('lable2_name').string
				for label1 in soup.find_all('SECTION', {"id": "_label1"}):
					for protocol in label1.find_all('VALUE'):
						str_ += '<SECTION: label1>' + '\n'
						str_ += protocol.text

				for label3 in soup.find_all('SECTION', {"id": "_label3"}):
					for comment in label3.find_all('VALUE'):
						str_ += '\n'
						str_ += '<SECTION: label3> \n'
						str_ += comment.text

				category1 += str_

				if not os.path.exists(outdir + input_folder):
				    os.makedirs(outdir + '/' +input_folder)
				try:
					with open(outdir + '/' +  'name.txt', 'wb') as text_file:
						text_file.write(category1)
				except:
					pass
				break
	
	print 'Directory: ' + indir + ' finished'


def main():
	indir = sys.argv[1]
	outdir = sys.argv[2]
	run_parser(indir, outdir)


if __name__ == "__main__":
    main()



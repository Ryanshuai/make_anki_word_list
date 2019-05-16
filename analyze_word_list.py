import pylab as plt
from matplotlib_venn import venn3, venn3_circles


high_school_txt = 'D:/github_project/make_anki_word_list/word_list/high_school.txt'
college_cet4_txt = 'D:/github_project/make_anki_word_list/word_list/college_cet_4.txt'
college_cet6_txt = 'D:/github_project/make_anki_word_list/word_list/college_cet_6.txt'
college_post_txt = 'D:/github_project/make_anki_word_list/word_list/college_考研词汇表.txt'
toefl_qu_txt = 'D:/github_project/make_anki_word_list/word_list/曲根10000词汇表.txt'
toefl_red_txt = 'D:/github_project/make_anki_word_list/word_list/TOEFL_红宝书.txt'
toefl_class_txt = 'D:/github_project/make_anki_word_list/word_list/TOEFL_分类词汇.txt'
gre_3000_txt = 'D:/github_project/make_anki_word_list/word_list/GRE_3000.txt'
gre_foot_txt = 'D:/github_project/make_anki_word_list/word_list/GRE_佛脚词.txt'
gre_red_txt = 'D:/github_project/make_anki_word_list/word_list/GRE红宝书.txt'
gre_synonym_txt = 'D:/github_project/make_anki_word_list/word_list/GRE_synonym.txt'
internal_txt = 'D:/github_project/make_anki_word_list/word_list/internal_word.txt'
all_txt = 'D:/github_project/make_anki_word_list/word_list/all.txt'

input_txt_list = list()
# input_txt_list.append(high_school_txt)
# input_txt_list.append(college_cet4_txt)
# input_txt_list.append(college_cet6_txt)
# input_txt_list.append(college_post_txt)
# input_txt_list.append(toefl_qu_txt)
# input_txt_list.append(toefl_red_txt)
# input_txt_list.append(toefl_class_txt)
input_txt_list.append(gre_3000_txt)
# input_txt_list.append(gre_foot_txt)
input_txt_list.append(gre_red_txt)
input_txt_list.append(gre_synonym_txt)

set_list = list()
name_list = list()
for file in input_txt_list:
    with open(file, 'r', encoding='utf-8') as f:
        word_list = f.read().splitlines()
        set_list.append(set(word_list))
        name = file.split('/')[-1][:-4]
        name_list.append(name)

venn3(set_list, tuple(name_list))
# venn3(set_list, set_labels = ('A', 'B', 'C'))
plt.show()

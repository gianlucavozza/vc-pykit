#coding=utf-8
'''
Authors: G. Vozza, E. Bonetti
v. 0.1

This module: i) splits VCF files from Torrent Variant Caller;
ii) scans and retains only allele frequency > 0;
iii) creates multiple VCF files to comply with funcotator
'''
#modules
import sys

def split_vcf(query_file, output_file):
    out_file = open(output_file, 'w') #open new VCF file to write
    with open(query_file, "r") as query: #open query VCF to split
        for line in query:
            if line.startswith('#'): #add VCF header to the new file
                out_file.write(line)
                continue
            split_line = line.strip().split('\t')
            info = split_line[7]
            info_gt = split_line[9] # le informazioni su genotipo, AF ecc. sono contenute nella colonna numero 9
            alt = split_line[4]
            if ',' in alt:
                alt_array = alt.split(',') #create an array with all the alterations in the same position
                n_alternative = len(alt_array) #get the number of alterations in the position as an integer
                info_split = info.split(';')
                info_gt_split = info_gt.split(':')
                for i in range(0, n_alternative):
                    string_to_write = '\t'.join(split_line[0:4]) + '\t' + alt_array[i] + '\t' + split_line[5] + '\t' + split_line[6] + '\t' #write many rows as the number of the alterations at the same position
                    for element in info_split:
                        split_element = element.split('=')
                        info_symbol = split_element[0]
                        if ',' in split_element[1]:
                            if len(split_element[1].split(',')) < n_alternative: #if elements number is not the same of the number of alternatives then assign the whole string to all the alternatives
                                info_value = split_element[1]
                            else:
                                info_value = split_element[1].split(',')[i]
                            string_to_write = string_to_write + info_symbol + '=' + info_value + ';'
                        else:
                            info_value = split_element[1]
                            string_to_write = string_to_write + info_symbol + '=' + info_value + ';'
                    string_to_write = string_to_write[:-1] #remove ';' at the end of the line
                    string_to_write = string_to_write + '\t' + split_line[8] + '\t' + info_gt + '\n'
                    out_file.write(string_to_write)
            else:
                out_file.write(line)
    out_file.close()

def scan_af(query_file, output_file):
    out_file = open(output_file, 'w') #open new VCF file to write
    with open(query_file, "r") as query: #open query VCF to split
        for line in query:
            if line.startswith('#'): #add VCF header to the new file
                out_file.write(line)
                continue
            split_line = line.strip().split('\t')
            info = split_line[7]
            af = info.split(';')[0].split('=')[1] #get allele frequency
            if float(af) > 0:
                out_file.write(line)
    out_file.close()

def funco_vcf(query_file):
    header = ''
    first_pos = True
    pos_to_check = ''
    with open(query_file, "r") as query: #open query VCF to split
        for line in query:
            if line.startswith('#'): #add VCF header to the new file
                header = header + line
                continue
            split_line = line.strip().split('\t')
            pos = split_line[1]
            ref = split_line[3]
            alt = split_line[4]
            if first_pos:
                pos_to_check = pos
                first_pos = False 
                continue
            if pos_to_check == pos:
                out = open(query_file[:-4] + '_' + pos + '_' + ref + '_' + alt + '.vcf', 'w')
                out.write(header)
                out.write(line)
                pos_to_check = pos
            else:
                pos_to_check = pos



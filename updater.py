from __future__ import unicode_literals
import sys

# -*- coding: utf-8 -*-

sys.path.append("/home/coronavi/.local/lib/python2.7/site-packages")
sys.path.append("/home/coronavi/.local/lib/python2.7/site-packages")
import numpy as np
import pandas as pd
from time import gmtime, strftime
from lxml import html
import requests
import pandas as pd

dir = 'https://www.worldometers.info/coronavirus/#countries'
df = pd.read_html(dir)[0]
try:
    df['NewCases'] = df['NewCases'].replace({'\$': '', ',': ''}, regex=True)
except:
    pass
df = df.replace('S. Korea','South Korea')
df = df.replace('UK','United Kingdom')
df = df.replace('USA','United States')
df = df.replace('Czechia','Czech Republic',)
df = df.rename(columns={'Tot\xa0Cases/1M pop':'PerMil','Country,Other':'Country','Serious,Critical':'CriticalCases'})
df = df.sort_values('Country')
df = df.fillna(0)
df = df[df.Country != 'Diamond Princess']
df = df[df.Country != 'Faeroe Islands']

df = df[df.Country != 'North Macedonia']
df = df[df.Country != 'Total:']

totalcases = df.TotalCases.tolist()
newcases = df.NewCases.tolist()
totaldeaths = df.TotalDeaths.tolist()
newdeaths = df.NewDeaths.tolist()
activecases = df.ActiveCases.tolist()
totalrecovered = df.TotalRecovered.tolist()
criticalcases = df.CriticalCases.tolist()
permil = df.PerMil.tolist()

countries_dict = {'AF': 'Afghanistan',
'AL': 'Albania',
'DZ': 'Algeria',
'AS': 'American Samoa',
'AD': 'Andorra',
'AO': 'Angola',
'AI': 'Anguilla',
'AQ': 'Antarctica',
'AG': 'Antigua and Barbuda',
'AR': 'Argentina',
'AM': 'Armenia',
'AW': 'Aruba',
'AU': 'Australia',
'AT': 'Austria',
'AZ': 'Azerbaijan',
'BS': 'Bahamas',
'BH': 'Bahrain',
'BD': 'Bangladesh',
'BB': 'Barbados',
'BY': 'Belarus',
'BE': 'Belgium',
'BZ': 'Belize',
'BJ': 'Benin',
'BM': 'Bermuda',
'BT': 'Bhutan',
'BO': 'Bolivia',
'BA': 'Bosnia and Herzegovina',
'BW': 'Botswana',
'BR': 'Brazil',
'IO': 'British Indian Ocean Territory',
'VG': 'British Virgin Islands',
'BN': 'Brunei Darussalam',
'BG': 'Bulgaria',
'BF': 'Burkina Faso',
'BI': 'Burundi',
'KH': 'Cambodia',
'CM': 'Cameroon',
'CA': 'Canada',
'CV': 'Cape Verde',
'BQ': 'Caribbean Netherlands',
'KY': 'Cayman Islands',
'CF': 'Central African Republic',
'TD': 'Chad',
'CL': 'Chile',
'CN': 'China',
'CX': 'Christmas Island',
'CC': 'Cocos Islands',
'CO': 'Colombia',
'KM': 'Comoros',
'CG': 'Congo',
'CK': 'Cook Islands',
'CR': 'Costa Rica',
'HR': 'Croatia',
'CU': 'Cuba',
'CW': 'Curaçao',
'CY': 'Cyprus',
'CZ': 'Czech Republic',
'CD': 'Democratic Republic of the Congo',
'DK': 'Denmark',
'DJ': 'Djibouti',
'DM': 'Dominica',
'DO': 'Dominican Republic',
'EC': 'Ecuador',
'EG': 'Egypt',
'SV': 'El Salvador',
'GQ': 'Equatorial Guinea',
'ER': 'Eritrea',
'EE': 'Estonia',
'ET': 'Ethiopia',
'FK': 'Falkland Islands',
'FO': 'Faroe Islands',
'FM': 'Federated States of Micronesia',
'FJ': 'Fiji',
'FI': 'Finland',
'FR': 'France',
'GF': 'French Guiana',
'PF': 'French Polynesia',
'TF': 'French Southern Territories',
'GA': 'Gabon',
'GM': 'Gambia',
'GE': 'Georgia',
'DE': 'Germany',
'GH': 'Ghana',
'GI': 'Gibraltar',
'GR': 'Greece',
'GL': 'Greenland',
'GD': 'Grenada',
'GP': 'Guadeloupe',
'GU': 'Guam',
'GT': 'Guatemala',
'GN': 'Guinea',
'GW': 'Guinea-Bissau',
'GY': 'Guyana',
'HT': 'Haiti',
'HN': 'Honduras',
'HK': 'Hong Kong',
'HU': 'Hungary',
'IS': 'Iceland',
'IN': 'India',
'ID': 'Indonesia',
'IR': 'Iran',
'IQ': 'Iraq',
'IE': 'Ireland',
'IM': 'Isle of Man',
'IL': 'Israel',
'IT': 'Italy',
'CI': 'Ivory Coast',
'JM': 'Jamaica',
'JP': 'Japan',
'JE': 'Jersey',
'JO': 'Jordan',
'KZ': 'Kazakhstan',
'KE': 'Kenya',
'KI': 'Kiribati',
'XK': 'Kosovo',
'KW': 'Kuwait',
'KG': 'Kyrgyzstan',
'LA': 'Laos',
'LV': 'Latvia',
'LB': 'Lebanon',
'LS': 'Lesotho',
'LR': 'Liberia',
'LY': 'Libya',
'LI': 'Liechtenstein',
'LT': 'Lithuania',
'LU': 'Luxembourg',
'MO': 'Macau',
'MK': 'Macedonia',
'MG': 'Madagascar',
'MW': 'Malawi',
'MY': 'Malaysia',
'MV': 'Maldives',
'ML': 'Mali',
'MT': 'Malta',
'MH': 'Marshall Islands',
'MQ': 'Martinique',
'MR': 'Mauritania',
'MU': 'Mauritius',
'YT': 'Mayotte',
'MX': 'Mexico',
'MD': 'Moldova',
'MC': 'Monaco',
'MN': 'Mongolia',
'ME': 'Montenegro',
'MS': 'Montserrat',
'MA': 'Morocco',
'MZ': 'Mozambique',
'MM': 'Myanmar',
'NA': 'Namibia',
'NR': 'Nauru',
'NP': 'Nepal',
'NL': 'Netherlands',
'NC': 'New Caledonia',
'NZ': 'New Zealand',
'NI': 'Nicaragua',
'NE': 'Niger',
'NG': 'Nigeria',
'NU': 'Niue',
'NF': 'Norfolk Island',
'KP': 'North Korea',
'MP': 'Northern Mariana Islands',
'NO': 'Norway',
'OM': 'Oman',
'PK': 'Pakistan',
'PW': 'Palau',
'PS': 'Palestine',
'PA': 'Panama',
'PG': 'Papua New Guinea',
'PY': 'Paraguay',
'PE': 'Peru',
'PH': 'Philippines',
'PN': 'Pitcairn Islands',
'PL': 'Poland',
'PT': 'Portugal',
'PR': 'Puerto Rico',
'QA': 'Qatar',
'RE': 'Reunion',
'RO': 'Romania',
'RU': 'Russia',
'RW': 'Rwanda',
'SH': 'Saint Helena',
'KN': 'Saint Kitts and Nevis',
'LC': 'Saint Lucia',
'PM': 'Saint Pierre and Miquelon',
'VC': 'Saint Vincent and the Grenadines',
'WS': 'Samoa',
'SM': 'San Marino',
'ST': 'São Tomé and Príncipe',
'SA': 'Saudi Arabia',
'SN': 'Senegal',
'RS': 'Serbia',
'SC': 'Seychelles',
'SL': 'Sierra Leone',
'SG': 'Singapore',
'SX': 'Sint Maarten',
'SK': 'Slovakia',
'SI': 'Slovenia',
'SB': 'Solomon Islands',
'SO': 'Somalia',
'ZA': 'South Africa',
'GS': 'South Georgia and the South Sandwich Islands',
'KR': 'South Korea',
'SS': 'South Sudan',
'ES': 'Spain',
'LK': 'Sri Lanka',
'SD': 'Sudan',
'SR': 'Suriname',
'SJ': 'Svalbard and Jan Mayen',
'SZ': 'Eswatini',
'SE': 'Sweden',
'CH': 'Switzerland',
'SY': 'Syria',
'TW': 'Taiwan',
'TJ': 'Tajikistan',
'TZ': 'Tanzania',
'TH': 'Thailand',
'TL': 'Timor-Leste',
'TG': 'Togo',
'TK': 'Tokelau',
'TO': 'Tonga',
'TT': 'Trinidad and Tobago',
'TN': 'Tunisia',
'TR': 'Turkey',
'TM': 'Turkmenistan',
'TC': 'Turks and Caicos Islands',
'TV': 'Tuvalu',
'UG': 'Uganda',
'UA': 'Ukraine',
'AE': 'United Arab Emirates',
'GB': 'United Kingdom',
'US': 'United States',
'UM': 'United States Minor Outlying Islands',
'VI': 'United States Virgin Islands',
'UY': 'Uruguay',
'UZ': 'Uzbekistan',
'VU': 'Vanuatu',
'VA': 'Vatican City',
'VE': 'Venezuela',
'VN': 'Vietnam',
'WF': 'Wallis and Futuna',
'EH': 'Western Sahara',
'YE': 'Yemen',
'ZM': 'Zambia',
'ZW': 'Zimbabwe'}

countriesName = list(countries_dict.values())
countriesShort = countries_dict.keys()
countriesData = list(df.Country)

datastring = ''

for country in countriesName:
    if country not in countriesData:
        df = df[~df['Country'].isin([country])]

df = df.set_index(df.Country)

rev = {y:x for x,y in countries_dict.items()}

for index, row in df.iterrows():
    if row['Country'] in rev:
        x = rev[row['Country']]+": {"
        x += 'totalcases: '+ str(row['TotalCases'])
        x += ', newcases: '+str(row['NewCases'])
        x += ', totaldeaths: '+str(row['TotalDeaths'])
        x += ', newdeaths: '+str(row['NewDeaths'])
        x += ', activecases: '+str(row['ActiveCases'])
        x += ', totalrecovered: '+str(row['TotalRecovered'])
        x += ', criticalcases: '+str(row['CriticalCases'])
        x += ', permil: '+str(row['PerMil'])
        x += '},\n'
        datastring += x
datastring += '} \n } \n'

hardstring = ""
with open('/home/coronavi/public_html/hardcode.txt','r') as hardcodef:
    for line in hardcodef:
        hardstring += line

with open('/home/coronavi/public_html/population.js','w') as jsf:
    jsf.write(hardstring+datastring)

header = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"
}

page = requests.get('https://www.worldometers.info/coronavirus/',headers=header)
tree = html.fromstring(page.content)

def puller():
    '''Returns three data values from html page'''
    page = requests.get('https://www.worldometers.info/coronavirus/')
    html_string = str(page.content)
    totalcases_substring = '<span style="color:#aaa'
    if totalcases_substring in html_string:
        ind = html_string.index(totalcases_substring)
        totalcasesnum = html_string[ind+15:ind+40]
        totalcasesnum = ''.join(x for x in totalcasesnum if x.isdecimal())
        totalcasesnum = f"{int(totalcasesnum):,d}"
    deaths_substring = '<div class="maincounter-number"> <span>'
    if deaths_substring in html_string:
        ind = html_string.index(deaths_substring)
        deathsnum = html_string[ind+20:ind+67]
        deathsnum = ''.join(x for x in deathsnum if x.isdecimal())
        deathsnum = f"{int(deathsnum):,d}"
    recovered_substring = '<h1>Recovered:</h1>'
    if recovered_substring in html_string:
        ind = html_string.index(recovered_substring)
        recoverednum = html_string[ind+75:ind+111]
        recoverednum = ''.join(x for x in recoverednum if x.isdecimal())
        recoverednum = f"{int(recoverednum):,d}"
    return (totalcasesnum,deathsnum,recoverednum)

stats = puller()


indexhardstring = ""

def Linefinder(lines):
    '''Finds version line and returns the index'''
    for line in lines:
        if 'version=z' in line:
            return lines.index(line)
        else:
            continue

def Titlefinder(lines):
    '''Finds version line and returns the index'''
    for line in lines:
        if '<h1><center>Interactive' in line:
            return lines.index(line)
        else:
            continue

def caseslinefinder(lines):
    '''Finds version line and returns the index'''
    for line in lines:
        if '<div class="cases">' in line:
            return lines.index(line)
        else:
            continue

def deathslinefinder(lines):
    '''Finds version line and returns the index'''
    for line in lines:
        if '<div class="deaths">' in line:
            return lines.index(line)
        else:
            continue

def recoveredlinefinder(lines):
    '''Finds version line and returns the index'''
    for line in lines:
        if '<div class="recovered">' in line:
            return lines.index(line)
        else:
            continue

timestr = strftime("%d-%B-%Y %H:%M", gmtime())

with open('/home/coronavi/public_html/index.html','r') as indexfileread:
        lines = indexfileread.readlines()
        line_index = Linefinder(lines)
        version_num = lines[line_index][lines[line_index].index('z')+1:lines[line_index].index('Z')]
        version_num = int(version_num)
        version_num += 1
        newline = "<script src=\"population.js?version=z"+str(version_num)+"Z\"></script>\n"
        lines[line_index] = newline

        titleindex = Titlefinder(lines)
        lines[titleindex] = '<h1><center>Interactive Coronavirus Map Live\n'

        casesline = '<h3><center> <div class="cases">Cases: '+ stats[0] +'</div></h3>\n'
        deathline = '<h3><center> <div class="deaths"> Deaths: ' +stats[1]+ '</h3>\n'
        recoveredline = '<h3><center> <div class="recovered">Recovered: ' + stats[2]+'</h3>\n'
        caseslineind = caseslinefinder(lines)
        deathslineind = deathslinefinder(lines)
        recoveredlineind = recoveredlinefinder(lines)
        lines[caseslineind] = casesline
        lines[deathslineind] = deathline
        lines[recoveredlineind] = recoveredline
        print(lines)

with open('/home/coronavi/public_html/index.html','w') as indexfilewrite:
        indexfilewrite.writelines(lines)


print("Website updated succesfully.")

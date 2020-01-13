# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 12:32:11 2019

@author: soumik
"""

from flask import Blueprint

mod = Blueprint ('dictionary',__name__)

def CountryCode():
    CountryCodeDict = ['^AF$',
    '^AL$',
    '^DZ$',
    '^AS$',
    '^AD$',
    '^AO$',
    '^AI$',
    '^AQ$',
    '^AG$',
    '^AR$',
    '^AM$',
    '^AW$',
    '^AU$',
    '^AT$',
    '^AZ$',
    '^BS$',
    '^BH$',
    '^BD$',
    '^BB$',
    '^BY$',
    '^BE$',
    '^BZ$',
    '^BJ$',
    '^BM$',
    '^BT$',
    '^BO$',
    '^BA$',
    '^BW$',
    '^BV$',
    '^BR$',
    '^IO$',
    '^BN$',
    '^BG$',
    '^BF$',
    '^BI$',
    '^KH$',
    '^CM$',
    '^CA$',
    '^CV$',
    '^KY$',
    '^CF$',
    '^TD$',
    '^CL$',
    '^CN$',
    '^CX$',
    '^CC$',
    '^CO$',
    '^KM$',
    '^CD$',
    '^CG$',
    '^CK$',
    '^CR$',
    '^CI$',
    '^HR$',
    '^CU$',
    '^CY$',
    '^CZ$',
    '^CS$',
    '^DK$',
    '^DJ$',
    '^DM$',
    '^DO$',
    '^TP$',
    '^EC$',
    '^EG$',
    '^SV$',
    '^GQ$',
    '^ER$',
    '^EE$',
    '^ET$',
    '^FK$',
    '^FO$',
    '^FJ$',
    '^FI$',
    '^FR$',
    '^GF$',
    '^PF$',
    '^TF$',
    '^GA$',
    '^GM$',
    '^GE$',
    '^DE$',
    '^GH$',
    '^GI$',
    '^GB$',
    '^GR$',
    '^GL$',
    '^GD$',
    '^GP$',
    '^GU$',
    '^GT$',
    '^GN$',
    '^GW$',
    '^GY$',
    '^HT$',
    '^HM$',
    '^VA$',
    '^HN$',
    '^HK$',
    '^HU$',
    '^IS$',
    '^IN$',
    '^ID$',
    '^IR$',
    '^IQ$',
    '^IE$',
    '^IL$',
    '^IT$',
    '^JM$',
    '^JP$',
    '^JO$',
    '^KZ$',
    '^KE$',
    '^KI$',
    '^KP$',
    '^KR$',
    '^KW$',
    '^KG$',
    '^LA$',
    '^LV$',
    '^LB$',
    '^LS$',
    '^LR$',
    '^LY$',
    '^LI$',
    '^LT$',
    '^LU$',
    '^MO$',
    '^MK$',
    '^MG$',
    '^MW$',
    '^MY$',
    '^MV$',
    '^ML$',
    '^MT$',
    '^MH$',
    '^MQ$',
    '^MR$',
    '^MU$',
    '^YT$',
    '^MX$',
    '^FM$',
    '^MD$',
    '^MC$',
    '^MN$',
    '^MS$',
    '^MA$',
    '^MZ$',
    '^MM$',
    '^NA$',
    '^NR$',
    '^NP$',
    '^NL$',
    '^AN$',
    '^NC$',
    '^NZ$',
    '^NI$',
    '^NE$',
    '^NG$',
    '^NU$',
    '^NF$',
    '^MP$',
    '^NO$',
    '^OM$',
    '^PK$',
    '^PW$',
    '^PS$',
    '^PA$',
    '^PG$',
    '^PY$',
    '^PE$',
    '^PH$',
    '^PN$',
    '^PL$',
    '^PT$',
    '^PR$',
    '^QA$',
    '^RE$',
    '^RO$',
    '^SU$',
    '^RU$',
    '^RW$',
    '^SH$',
    '^KN$',
    '^LC$',
    '^PM$',
    '^VC$',
    '^WS$',
    '^SM$',
    '^ST$',
    '^SA$',
    '^RS$',
    '^SN$',
    '^SC$',
    '^SL$',
    '^SG$',
    '^SK$',
    '^SI$',
    '^SB$',
    '^SO$',
    '^ZA$',
    '^GS$',
    '^ES$',
    '^LK$',
    '^SD$',
    '^SR$',
    '^SJ$',
    '^SZ$',
    '^SE$',
    '^CH$',
    '^SY$',
    '^TW$',
    '^TJ$',
    '^TZ$',
    '^TH$',
    '^TG$',
    '^TK$',
    '^TO$',
    '^TT$',
    '^TE$',
    '^TN$',
    '^TR$',
    '^TM$',
    '^TC$',
    '^TV$',
    '^UG$',
    '^UA$',
    '^AE$',
    '^GB$',
    '^US$',
    '^UM$',
    '^UY$',
    '^UZ$',
    '^VU$',
    '^VA$',
    '^VE$',
    '^VN$',
    '^VI$',
    '^VQ$',
    '^WF$',
    '^EH$',
    '^YE$',
    '^YU$',
    '^ZR$',
    '^ZM$',
    '^ZW$',
    '^UK$'
    ]
    
    return CountryCodeDict



def CountryName():
    CountryNameDict = ['^Afghanistan $',
    '^Albania $',
    '^Algeria $',
    '^American Samoa $',
    '^Andorra $',
    '^Angola $',
    '^Anguilla $',
    '^Antigua & Barbuda $',
    '^Argentina $',
    '^Armenia $',
    '^Aruba $',
    '^Australia $',
    '^Austria $',
    '^Azerbaijan $',
    '^Bahamas, The $',
    '^Bahrain $',
    '^Bangladesh $',
    '^Barbados $',
    '^Belarus $',
    '^Belgium $',
    '^Belize $',
    '^Benin $',
    '^Bermuda $',
    '^Bhutan $',
    '^Bolivia $',
    '^Bosnia & Herzegovina $',
    '^Botswana $',
    '^Brazil $',
    '^British Virgin Is. $',
    '^Brunei $',
    '^Bulgaria $',
    '^Burkina Faso $',
    '^Burma $',
    '^Burundi $',
    '^Cambodia $',
    '^Cameroon $',
    '^Canada $',
    '^Cape Verde $',
    '^Cayman Islands $',
    '^Central African Rep. $',
    '^Chad $',
    '^Chile $',
    '^China $',
    '^Colombia $',
    '^Comoros $',
    '^Congo, Dem. Rep. $',
    '^Congo, Repub. of the $',
    '^Cook Islands $',
    '^Costa Rica $',
    "^Cote d'Ivoire $",
    '^Croatia $',
    '^Cuba $',
    '^Cyprus $',
    '^Czech Republic $',
    '^Denmark $',
    '^Djibouti $',
    '^Dominica $',
    '^Dominican Republic $',
    '^East Timor $',
    '^Ecuador $',
    '^Egypt $',
    '^El Salvador $',
    '^Equatorial Guinea $',
    '^Eritrea $',
    '^Estonia $',
    '^Ethiopia $',
    '^Faroe Islands $',
    '^Fiji $',
    '^Finland $',
    '^France $',
    '^French Guiana $',
    '^French Polynesia $',
    '^Gabon $',
    '^Gambia, The $',
    '^Gaza Strip $',
    '^Georgia $',
    '^Germany $',
    '^Ghana $',
    '^Gibraltar $',
    '^Greece $',
    '^Greenland $',
    '^Grenada $',
    '^Guadeloupe $',
    '^Guam $',
    '^Guatemala $',
    '^Guernsey $',
    '^Guinea $',
    '^Guinea-Bissau $',
    '^Guyana $',
    '^Haiti $',
    '^Honduras $',
    '^Hong Kong $',
    '^Hungary $',
    '^Iceland $',
    '^India $',
    '^Indonesia $',
    '^Iran $',
    '^Iraq $',
    '^Ireland $',
    '^Isle of Man $',
    '^Israel $',
    '^Italy $',
    '^Jamaica $',
    '^Japan $',
    '^Jersey $',
    '^Jordan $',
    '^Kazakhstan $',
    '^Kenya $',
    '^Kiribati $',
    '^Korea, North $',
    '^Korea, South $',
    '^Kuwait $',
    '^Kyrgyzstan $',
    '^Laos $',
    '^Latvia $',
    '^Lebanon $',
    '^Lesotho $',
    '^Liberia $',
    '^Libya $',
    '^Liechtenstein $',
    '^Lithuania $',
    '^Luxembourg $',
    '^Macau $',
    '^Macedonia $',
    '^Madagascar $',
    '^Malawi $',
    '^Malaysia $',
    '^Maldives $',
    '^Mali $',
    '^Malta $',
    '^Marshall Islands $',
    '^Martinique $',
    '^Mauritania $',
    '^Mauritius $',
    '^Mayotte $',
    '^Mexico $',
    '^Micronesia, Fed. St. $',
    '^Moldova $',
    '^Monaco $',
    '^Mongolia $',
    '^Montserrat $',
    '^Morocco $',
    '^Mozambique $',
    '^Namibia $',
    '^Nauru $',
    '^Nepal $',
    '^Netherlands $',
    '^Netherlands Antilles $',
    '^New Caledonia $',
    '^New Zealand $',
    '^Nicaragua $',
    '^Niger $',
    '^Nigeria $',
    '^N. Mariana Islands $',
    '^Norway $',
    '^Oman $',
    '^Pakistan $',
    '^Palau $',
    '^Panama $',
    '^Papua New Guinea $',
    '^Paraguay $',
    '^Peru $',
    '^Philippines $',
    '^Poland $',
    '^Portugal $',
    '^Puerto Rico $',
    '^Qatar $',
    '^Reunion $',
    '^Romania $',
    '^Russia $',
    '^Rwanda $',
    '^Saint Helena $',
    '^Saint Kitts & Nevis $',
    '^Saint Lucia $',
    '^St Pierre & Miquelon $',
    '^Saint Vincent and the Grenadines $',
    '^Samoa $',
    '^San Marino $',
    '^Sao Tome & Principe $',
    '^Saudi Arabia $',
    '^Senegal $',
    '^Serbia $',
    '^Seychelles $',
    '^Sierra Leone $',
    '^Singapore $',
    '^Slovakia $',
    '^Slovenia $',
    '^Solomon Islands $',
    '^Somalia $',
    '^South Africa $',
    '^Spain $',
    '^Sri Lanka $',
    '^Sudan $',
    '^Suriname $',
    '^Swaziland $',
    '^Sweden $',
    '^Switzerland $',
    '^Syria $',
    '^Taiwan $',
    '^Tajikistan $',
    '^Tanzania $',
    '^Thailand $',
    '^Togo $',
    '^Tonga $',
    '^Trinidad & Tobago $',
    '^Tunisia $',
    '^Turkey $',
    '^Turkmenistan $',
    '^Turks & Caicos Is $',
    '^Tuvalu $',
    '^Uganda $',
    '^Ukraine $',
    '^United Arab Emirates $',
    '^United Kingdom $',
    '^United States $',
    '^Uruguay $',
    '^Uzbekistan $',
    '^Vanuatu $',
    '^Venezuela $',
    '^Vietnam $',
    '^Virgin Islands $',
    '^Wallis and Futuna $',
    '^West Bank $',
    '^Western Sahara $',
    '^Yemen $',
    '^Zambia $',
    '^Zimbabwe $'
    ]
    return CountryNameDict
import pandas as pd
df_raw=pd.read_excel('C:/Users/홍예지/Desktop/프릭스헬스케어/work/milestone.xlsx')
#print(df_2)
df_refine=df_raw

# 중복제거
df_refine.drop_duplicates()

df_refine['created_at'] = df_refine['created_at'].astype(str)
df_refine['updated_at'] = df_refine['created_at'].astype(str)


df_temporary_1=pd.DataFrame()
df_temporary_2=pd.DataFrame()
df_temporary_1=df_refine['created_at'].str.split(" ")
df_temporary_2=df_refine['updated_at'].str.split(" ")
df_temporary_1=df_temporary_1.str[-1]
df_temporary_2=df_temporary_2.str[-1]

result = pd.concat([df_refine,df_temporary_1,df_temporary_2],axis=1)
result.columns=['person','milestone','grade','done_day_after_birth','created_at','updated_at','created_hour','updated_hour']

# 00시 제거
final_result=pd.DataFrame()
final_result=result[result.created_hour!='00:00:00.000']
print(final_result)

# milestone_number / unique_milestone_number mapping
raw_data=pd.DataFrame()
raw_data=final_result


raw_data.loc[(raw_data['milestone'] == 439) | (raw_data['milestone']== 516) | (raw_data['milestone']== 554),'milestone_unique']= 2
raw_data.loc[(raw_data['milestone'] == 638) | (raw_data['milestone']== 677),'milestone_unique']= 3
raw_data.loc[(raw_data['milestone'] == 39) | (raw_data['milestone']== 77) | (raw_data['milestone']== 115),'milestone_unique']= 4
raw_data.loc[(raw_data['milestone'] == 319),'milestone_unique']= 5
raw_data.loc[(raw_data['milestone'] == 37) | (raw_data['milestone']== 75) ,'milestone_unique']= 6
raw_data.loc[(raw_data['milestone'] == 717) | (raw_data['milestone']== 756) | (raw_data['milestone']== 796),'milestone_unique']= 7
raw_data.loc[(raw_data['milestone'] == 40) | (raw_data['milestone']== 78) | (raw_data['milestone']== 116)| (raw_data['milestone']== 153),'milestone_unique']= 8
raw_data.loc[(raw_data['milestone'] == 519) | (raw_data['milestone']== 557) | (raw_data['milestone']== 595),'milestone_unique']= 9
raw_data.loc[(raw_data['milestone'] == 560) | (raw_data['milestone']== 597) | (raw_data['milestone']== 633)| (raw_data['milestone']== 673),'milestone_unique']= 10
raw_data.loc[(raw_data['milestone'] == 199) | (raw_data['milestone']== 236) | (raw_data['milestone']== 274),'milestone_unique']= 11
raw_data.loc[(raw_data['milestone'] == 119) | (raw_data['milestone']== 156) | (raw_data['milestone']== 193),'milestone_unique']= 12
raw_data.loc[(raw_data['milestone'] == 598) | (raw_data['milestone']== 634) | (raw_data['milestone']== 674),'milestone_unique']= 13
raw_data.loc[(raw_data['milestone'] == 718) | (raw_data['milestone']== 757) | (raw_data['milestone']== 797),'milestone_unique']= 14
raw_data.loc[(raw_data['milestone'] == 599) | (raw_data['milestone']== 635),'milestone_unique']= 15
raw_data.loc[(raw_data['milestone'] == 400) | (raw_data['milestone']== 437) | (raw_data['milestone']== 477)| (raw_data['milestone']== 514)| (raw_data['milestone']== 553),'milestone_unique']= 16
raw_data.loc[(raw_data['milestone'] == 520) | (raw_data['milestone']== 558) | (raw_data['milestone']== 596),'milestone_unique']= 17
raw_data.loc[(raw_data['milestone'] == 640) | (raw_data['milestone']== 679) | (raw_data['milestone']== 715) | (raw_data['milestone']== 754)| (raw_data['milestone']== 794),'milestone_unique']= 18
raw_data.loc[(raw_data['milestone'] == 240) | (raw_data['milestone']== 278),'milestone_unique']= 19
raw_data.loc[(raw_data['milestone'] == 320) | (raw_data['milestone']== 358) | (raw_data['milestone']== 396),'milestone_unique']= 20
raw_data.loc[(raw_data['milestone'] == 600) | (raw_data['milestone']== 636) | (raw_data['milestone']== 675),'milestone_unique']= 21
raw_data.loc[(raw_data['milestone'] == 719) | (raw_data['milestone']== 758) | (raw_data['milestone']== 798),'milestone_unique']= 22
raw_data.loc[(raw_data['milestone'] == 34) | (raw_data['milestone']== 73) | (raw_data['milestone']== 113),'milestone_unique']= 23
raw_data.loc[(raw_data['milestone'] == 316) | (raw_data['milestone']== 355) | (raw_data['milestone']== 393),'milestone_unique']= 24
raw_data.loc[(raw_data['milestone'] == 433) | (raw_data['milestone']== 473) ,'milestone_unique']= 25
raw_data.loc[(raw_data['milestone'] == 198) | (raw_data['milestone']== 235) ,'milestone_unique']= 26
raw_data.loc[(raw_data['milestone'] == 38) | (raw_data['milestone']== 76) | (raw_data['milestone']== 114),'milestone_unique']= 27
raw_data.loc[(raw_data['milestone'] == 36) | (raw_data['milestone']== 74) ,'milestone_unique']= 28
raw_data.loc[(raw_data['milestone'] == 238) | (raw_data['milestone']== 276) | (raw_data['milestone']== 313),'milestone_unique']= 29
raw_data.loc[(raw_data['milestone'] == 158) | (raw_data['milestone']== 195) | (raw_data['milestone']== 233) ,'milestone_unique']= 30
raw_data.loc[(raw_data['milestone'] == 120) | (raw_data['milestone']== 157) | (raw_data['milestone']== 194),'milestone_unique']= 31
raw_data.loc[(raw_data['milestone'] == 80) | (raw_data['milestone']== 118) | (raw_data['milestone']== 155) ,'milestone_unique']= 32
raw_data.loc[(raw_data['milestone'] == 159) | (raw_data['milestone']== 196) | (raw_data['milestone']== 234)| (raw_data['milestone']== 273),'milestone_unique']= 33
raw_data.loc[(raw_data['milestone'] == 200) | (raw_data['milestone']== 237) | (raw_data['milestone']== 275) ,'milestone_unique']= 34
raw_data.loc[(raw_data['milestone'] == 360) | (raw_data['milestone']== 398) ,'milestone_unique']= 35
raw_data.loc[(raw_data['milestone'] == 436) | (raw_data['milestone']== 476) | (raw_data['milestone']== 513) ,'milestone_unique']= 36
raw_data.loc[(raw_data['milestone'] == 239) | (raw_data['milestone']== 277) | (raw_data['milestone']== 314) | (raw_data['milestone']== 353) ,'milestone_unique']= 37
raw_data.loc[(raw_data['milestone'] == 35) ,'milestone_unique']= 38
raw_data.loc[(raw_data['milestone'] == 480) | (raw_data['milestone']== 517) | (raw_data['milestone']== 555)| (raw_data['milestone']== 593) ,'milestone_unique']= 39
raw_data.loc[(raw_data['milestone'] == 33) ,'milestone_unique']= 40
raw_data.loc[(raw_data['milestone'] == 435) | (raw_data['milestone']== 475) ,'milestone_unique']= 41
raw_data.loc[(raw_data['milestone'] == 680) | (raw_data['milestone']== 716) | (raw_data['milestone']== 755) | (raw_data['milestone']== 795) ,'milestone_unique']= 42
raw_data.loc[(raw_data['milestone'] == 440) | (raw_data['milestone']== 479)  ,'milestone_unique']= 43
raw_data.loc[(raw_data['milestone'] == 518) | (raw_data['milestone']== 556) | (raw_data['milestone']== 594)  ,'milestone_unique']= 44
raw_data.loc[(raw_data['milestone'] == 637) | (raw_data['milestone']== 676) | (raw_data['milestone']== 713)  ,'milestone_unique']= 45
raw_data.loc[(raw_data['milestone'] == 438) | (raw_data['milestone']== 478) | (raw_data['milestone']== 515)  ,'milestone_unique']= 46
raw_data.loc[(raw_data['milestone'] == 399) ,'milestone_unique']= 47
raw_data.loc[(raw_data['milestone'] == 359) | (raw_data['milestone']== 397) | (raw_data['milestone']== 434)| (raw_data['milestone']== 474)  ,'milestone_unique']= 48
raw_data.loc[(raw_data['milestone'] == 160) | (raw_data['milestone']== 197) ,'milestone_unique']= 49
raw_data.loc[(raw_data['milestone'] == 639) | (raw_data['milestone']== 678) | (raw_data['milestone']== 714)| (raw_data['milestone']== 753)| (raw_data['milestone']== 793) ,'milestone_unique']= 50
raw_data.loc[(raw_data['milestone'] == 760) | (raw_data['milestone']== 800),'milestone_unique']= 51
raw_data.loc[(raw_data['milestone'] == 720) | (raw_data['milestone']== 759)|(raw_data['milestone']== 799),'milestone_unique']= 52
raw_data.loc[(raw_data['milestone'] == 559),'milestone_unique']= 53
raw_data.loc[(raw_data['milestone'] == 279) | (raw_data['milestone']== 315)|(raw_data['milestone']== 354),'milestone_unique']= 54
raw_data.loc[(raw_data['milestone'] == 318) | (raw_data['milestone']== 357)|(raw_data['milestone']== 395),'milestone_unique']= 55
raw_data.loc[(raw_data['milestone'] == 79) | (raw_data['milestone']== 117)|(raw_data['milestone']== 154),'milestone_unique']= 56
raw_data.loc[(raw_data['milestone'] == 176) | (raw_data['milestone']== 213)|(raw_data['milestone']== 251)|(raw_data['milestone']== 290)|(raw_data['milestone']== 329),'milestone_unique']= 57
raw_data.loc[(raw_data['milestone'] == 375) | (raw_data['milestone']== 413)|(raw_data['milestone']== 451)|(raw_data['milestone']== 490),'milestone_unique']= 58
raw_data.loc[(raw_data['milestone'] == 175)|(raw_data['milestone']== 212)|(raw_data['milestone']== 250)|(raw_data['milestone']== 289),'milestone_unique']= 59
raw_data.loc[(raw_data['milestone'] == 256)|(raw_data['milestone']== 294)|(raw_data['milestone']== 332)|(raw_data['milestone']== 370),'milestone_unique']= 60
raw_data.loc[(raw_data['milestone'] == 574)|(raw_data['milestone']== 614)|(raw_data['milestone']== 650),'milestone_unique']= 61
raw_data.loc[(raw_data['milestone'] == 696)|(raw_data['milestone']== 734)|(raw_data['milestone']== 772),'milestone_unique']= 62
raw_data.loc[(raw_data['milestone'] == 535)|(raw_data['milestone']== 572)|(raw_data['milestone']== 612),'milestone_unique']= 63
raw_data.loc[(raw_data['milestone'] == 55)|(raw_data['milestone']== 92)|(raw_data['milestone']== 130),'milestone_unique']= 64
raw_data.loc[(raw_data['milestone'] == 9),'milestone_unique']= 65
raw_data.loc[(raw_data['milestone'] == 13),'milestone_unique']= 66
raw_data.loc[(raw_data['milestone'] == 16)|(raw_data['milestone']== 53)|(raw_data['milestone']== 91)|(raw_data['milestone']== 129),'milestone_unique']= 67
raw_data.loc[(raw_data['milestone'] == 575),'milestone_unique']= 68
raw_data.loc[(raw_data['milestone'] == 776),'milestone_unique']= 69
raw_data.loc[(raw_data['milestone'] == 736)|(raw_data['milestone']== 774),'milestone_unique']= 70
raw_data.loc[(raw_data['milestone'] == 336)|(raw_data['milestone']== 374)|(raw_data['milestone']== 412)|(raw_data['milestone']== 450)|(raw_data['milestone']== 489),'milestone_unique']= 71
raw_data.loc[(raw_data['milestone'] == 136)|(raw_data['milestone']== 174)|(raw_data['milestone']== 211),'milestone_unique']= 72
raw_data.loc[(raw_data['milestone'] == 296)|(raw_data['milestone']== 334)|(raw_data['milestone']== 372),'milestone_unique']= 73
raw_data.loc[(raw_data['milestone'] == 616)|(raw_data['milestone']== 652),'milestone_unique']= 74
raw_data.loc[(raw_data['milestone'] == 655)|(raw_data['milestone']== 691)|(raw_data['milestone']== 730),'milestone_unique']= 75
raw_data.loc[(raw_data['milestone'] == 214)|(raw_data['milestone']== 252)|(raw_data['milestone']== 291)|(raw_data['milestone']== 295)|(raw_data['milestone']== 330)|(raw_data['milestone']== 333)|(raw_data['milestone']== 371)|(raw_data['milestone']== 410),'milestone_unique']= 76
raw_data.loc[(raw_data['milestone'] == 613)|(raw_data['milestone']== 649),'milestone_unique']= 77
raw_data.loc[(raw_data['milestone'] == 536)|(raw_data['milestone']== 573),'milestone_unique']= 78
raw_data.loc[(raw_data['milestone'] == 693)|(raw_data['milestone']== 732)|(raw_data['milestone']== 770),'milestone_unique']= 79
raw_data.loc[(raw_data['milestone'] == 653)|(raw_data['milestone']== 689),'milestone_unique']= 80
raw_data.loc[(raw_data['milestone'] == 10),'milestone_unique']= 81
raw_data.loc[(raw_data['milestone'] == 12),'milestone_unique']= 82
raw_data.loc[(raw_data['milestone'] == 335)|(raw_data['milestone']== 373),'milestone_unique']= 83
raw_data.loc[(raw_data['milestone'] == 54),'milestone_unique']= 84
raw_data.loc[(raw_data['milestone'] == 95)|(raw_data['milestone']== 133)|(raw_data['milestone']== 170)|(raw_data['milestone']== 209),'milestone_unique']= 85
raw_data.loc[(raw_data['milestone'] == 416)|(raw_data['milestone']== 454)|(raw_data['milestone']== 493)|(raw_data['milestone']== 530),'milestone_unique']= 86
raw_data.loc[(raw_data['milestone'] == 255)|(raw_data['milestone']== 293)|(raw_data['milestone']== 331)|(raw_data['milestone']== 369)|(raw_data['milestone']== 409),'milestone_unique']= 87
raw_data.loc[(raw_data['milestone'] == 415)|(raw_data['milestone']== 453)|(raw_data['milestone']== 492)|(raw_data['milestone']== 529),'milestone_unique']= 88
raw_data.loc[(raw_data['milestone'] == 533)|(raw_data['milestone']== 576),'milestone_unique']= 89
raw_data.loc[(raw_data['milestone'] == 615)|(raw_data['milestone']== 651),'milestone_unique']= 90
raw_data.loc[(raw_data['milestone'] == 694),'milestone_unique']= 91
raw_data.loc[(raw_data['milestone'] == 11)|(raw_data['milestone']== 49),'milestone_unique']= 92
raw_data.loc[(raw_data['milestone'] == 14)|(raw_data['milestone']== 51),'milestone_unique']= 93
raw_data.loc[(raw_data['milestone'] == 656)|(raw_data['milestone']== 692)|(raw_data['milestone']== 731)|(raw_data['milestone']== 769),'milestone_unique']= 94
raw_data.loc[(raw_data['milestone'] == 135)|(raw_data['milestone']== 173),'milestone_unique']= 95
raw_data.loc[(raw_data['milestone'] == 455)|(raw_data['milestone']== 494),'milestone_unique']= 96
raw_data.loc[(raw_data['milestone'] == 56)|(raw_data['milestone']== 93)|(raw_data['milestone']== 131)|(raw_data['milestone']== 169),'milestone_unique']= 97
raw_data.loc[(raw_data['milestone'] == 96)|(raw_data['milestone']== 134)|(raw_data['milestone']== 171),'milestone_unique']= 98
raw_data.loc[(raw_data['milestone'] == 496)|(raw_data['milestone']== 532)|(raw_data['milestone']== 570)|(raw_data['milestone']== 610),'milestone_unique']= 99
raw_data.loc[(raw_data['milestone'] == 376)|(raw_data['milestone']== 414)|(raw_data['milestone']== 452)|(raw_data['milestone']== 491),'milestone_unique']= 100
raw_data.loc[(raw_data['milestone'] == 456)|(raw_data['milestone']== 495)|(raw_data['milestone']== 531)|(raw_data['milestone']== 569)|(raw_data['milestone']== 609),'milestone_unique']= 102
raw_data.loc[(raw_data['milestone'] == 15)|(raw_data['milestone']== 52)|(raw_data['milestone']== 90),'milestone_unique']= 102
raw_data.loc[(raw_data['milestone'] == 172)|(raw_data['milestone']== 210)|(raw_data['milestone']== 249),'milestone_unique']= 103
raw_data.loc[(raw_data['milestone'] == 50)|(raw_data['milestone']== 89),'milestone_unique']= 104
raw_data.loc[(raw_data['milestone'] == 94)|(raw_data['milestone']== 132),'milestone_unique']= 105
raw_data.loc[(raw_data['milestone'] == 534)|(raw_data['milestone']== 571)|(raw_data['milestone']== 611),'milestone_unique']= 106
raw_data.loc[(raw_data['milestone'] == 654)|(raw_data['milestone']== 690)|(raw_data['milestone']== 729),'milestone_unique']= 107
raw_data.loc[(raw_data['milestone'] == 695)|(raw_data['milestone']== 733)|(raw_data['milestone']== 771),'milestone_unique']= 108
raw_data.loc[(raw_data['milestone'] == 735)|(raw_data['milestone']== 773),'milestone_unique']= 109
raw_data.loc[(raw_data['milestone'] == 775),'milestone_unique']= 110
raw_data.loc[(raw_data['milestone'] == 215)|(raw_data['milestone']== 253)|(raw_data['milestone']== 292),'milestone_unique']= 111
raw_data.loc[(raw_data['milestone'] == 216)|(raw_data['milestone']== 254),'milestone_unique']= 112
raw_data.loc[(raw_data['milestone'] == 647)|(raw_data['milestone']== 685)|(raw_data['milestone']== 722)|(raw_data['milestone']== 762),'milestone_unique']= 113
raw_data.loc[(raw_data['milestone'] == 88)|(raw_data['milestone']== 126)|(raw_data['milestone']== 163)|(raw_data['milestone']== 201),'milestone_unique']= 114
raw_data.loc[(raw_data['milestone'] == 85)|(raw_data['milestone']== 123),'milestone_unique']= 115
raw_data.loc[(raw_data['milestone'] == 86)|(raw_data['milestone']== 124)|(raw_data['milestone']== 161),'milestone_unique']= 116
raw_data.loc[(raw_data['milestone'] == 87)|(raw_data['milestone']== 125)|(raw_data['milestone']== 162),'milestone_unique']= 117
raw_data.loc[(raw_data['milestone'] == 402)|(raw_data['milestone']== 442)|(raw_data['milestone']== 481),'milestone_unique']= 118
raw_data.loc[(raw_data['milestone'] == 328)|(raw_data['milestone']== 365),'milestone_unique']= 119
raw_data.loc[(raw_data['milestone'] == 648)|(raw_data['milestone']== 686)|(raw_data['milestone']== 723)|(raw_data['milestone']== 763),'milestone_unique']= 120
raw_data.loc[(raw_data['milestone'] == 646)|(raw_data['milestone']== 684)|(raw_data['milestone']== 721)|(raw_data['milestone']== 761),'milestone_unique']= 121
raw_data.loc[(raw_data['milestone'] == 728)|(raw_data['milestone']== 768),'milestone_unique']= 122
raw_data.loc[(raw_data['milestone'] == 408),'milestone_unique']= 123
raw_data.loc[(raw_data['milestone'] == 725)|(raw_data['milestone']== 765),'milestone_unique']= 124
raw_data.loc[(raw_data['milestone'] == 247)|(raw_data['milestone']== 284)|(raw_data['milestone']== 287)|(raw_data['milestone']== 323)|(raw_data['milestone']== 326)|(raw_data['milestone']== 363),'milestone_unique']= 125
raw_data.loc[(raw_data['milestone'] == 404)|(raw_data['milestone']== 444),'milestone_unique']= 126
raw_data.loc[(raw_data['milestone'] == 367),'milestone_unique']= 127
raw_data.loc[(raw_data['milestone'] == 406)|(raw_data['milestone']== 446)|(raw_data['milestone']== 484),'milestone_unique']= 128
raw_data.loc[(raw_data['milestone'] == 3),'milestone_unique']= 129
raw_data.loc[(raw_data['milestone'] == 47)|(raw_data['milestone']== 83)|(raw_data['milestone']== 121),'milestone_unique']= 130
raw_data.loc[(raw_data['milestone'] == 7)|(raw_data['milestone']== 43),'milestone_unique']= 131
raw_data.loc[(raw_data['milestone'] == 727)|(raw_data['milestone']== 767),'milestone_unique']= 132
raw_data.loc[(raw_data['milestone'] == 207)|(raw_data['milestone']== 244)|(raw_data['milestone']== 281)|(raw_data['milestone']== 321),'milestone_unique']= 133
raw_data.loc[(raw_data['milestone'] == 246)|(raw_data['milestone']== 283)|(raw_data['milestone']== 322)|(raw_data['milestone']== 361),'milestone_unique']= 134
raw_data.loc[(raw_data['milestone'] == 1),'milestone_unique']= 135
raw_data.loc[(raw_data['milestone'] == 6)|(raw_data['milestone']== 42),'milestone_unique']= 136
raw_data.loc[(raw_data['milestone'] == 687)|(raw_data['milestone']== 724)|(raw_data['milestone']== 764),'milestone_unique']= 137
raw_data.loc[(raw_data['milestone'] == 368)|(raw_data['milestone']== 405)|(raw_data['milestone']== 445)|(raw_data['milestone']== 483),'milestone_unique']= 138
raw_data.loc[(raw_data['milestone'] == 45)|(raw_data['milestone']== 81),'milestone_unique']= 139
raw_data.loc[(raw_data['milestone'] == 567)|(raw_data['milestone']== 605)|(raw_data['milestone']== 642),'milestone_unique']= 140
raw_data.loc[(raw_data['milestone'] == 206) | (raw_data['milestone'] == 243), 'milestone_unique'] = 141
raw_data.loc[(raw_data['milestone'] == 607) | (raw_data['milestone'] == 644) | (raw_data['milestone'] == 682), 'milestone_unique'] = 142
raw_data.loc[(raw_data['milestone'] == 366) | (raw_data['milestone'] == 403) | (raw_data['milestone'] == 443) | (raw_data['milestone'] == 482), 'milestone_unique'] = 143
raw_data.loc[(raw_data['milestone'] == 526) | (raw_data['milestone'] == 564), 'milestone_unique'] = 144
raw_data.loc[(raw_data['milestone'] == 525) | (raw_data['milestone'] == 563) | (raw_data['milestone'] == 602), 'milestone_unique'] = 145
raw_data.loc[(raw_data['milestone'] == 208) | (raw_data['milestone'] == 245) | (raw_data['milestone'] == 282), 'milestone_unique'] = 146
raw_data.loc[(raw_data['milestone'] == 448) | (raw_data['milestone'] == 486) | (raw_data['milestone'] == 522), 'milestone_unique'] = 147
raw_data.loc[(raw_data['milestone'] == 487) | (raw_data['milestone'] == 523) | (raw_data['milestone'] == 561) | (raw_data['milestone'] == 608) | (raw_data['milestone'] == 645) | (raw_data['milestone'] == 683), 'milestone_unique'] = 148
raw_data.loc[(raw_data['milestone'] == 407) | (raw_data['milestone'] == 447) | (raw_data['milestone'] == 485) | (raw_data['milestone'] == 521), 'milestone_unique'] = 149
raw_data.loc[(raw_data['milestone'] == 528) | (raw_data['milestone'] == 566) | (raw_data['milestone'] == 604) | (raw_data['milestone'] == 641), 'milestone_unique'] = 150
raw_data.loc[(raw_data['milestone'] == 46) | (raw_data['milestone'] == 82) | (raw_data['milestone'] == 128) | (raw_data['milestone'] == 165) | (raw_data['milestone'] == 203), 'milestone_unique'] = 151
raw_data.loc[(raw_data['milestone'] == 8) | (raw_data['milestone'] == 44), 'milestone_unique'] = 152
raw_data.loc[(raw_data['milestone'] == 48) | (raw_data['milestone'] == 84) | (raw_data['milestone'] == 122), 'milestone_unique'] = 153
raw_data.loc[(raw_data['milestone'] == 2), 'milestone_unique'] = 154
raw_data.loc[(raw_data['milestone'] == 4), 'milestone_unique'] = 155
raw_data.loc[(raw_data['milestone'] == 5) | (raw_data['milestone'] == 41), 'milestone_unique'] = 156
raw_data.loc[(raw_data['milestone'] == 248) | (raw_data['milestone'] == 285) | (raw_data['milestone'] == 324) | (raw_data['milestone'] == 362), 'milestone_unique'] = 157
raw_data.loc[(raw_data['milestone'] == 288) | (raw_data['milestone'] == 327) | (raw_data['milestone'] == 364) | (raw_data['milestone'] == 401) | (raw_data['milestone'] == 441), 'milestone_unique'] = 158
raw_data.loc[(raw_data['milestone'] == 527) | (raw_data['milestone'] == 565) | (raw_data['milestone'] == 603), 'milestone_unique'] = 159
raw_data.loc[(raw_data['milestone'] == 688) | (raw_data['milestone'] == 726) | (raw_data['milestone'] == 766), 'milestone_unique'] = 160
raw_data.loc[(raw_data['milestone'] == 286) | (raw_data['milestone'] == 325), 'milestone_unique'] = 161
raw_data.loc[(raw_data['milestone'] == 488) | (raw_data['milestone'] == 524) | (raw_data['milestone'] == 562) | (raw_data['milestone'] == 601), 'milestone_unique'] = 162
raw_data.loc[(raw_data['milestone'] == 127) | (raw_data['milestone'] == 164) | (raw_data['milestone'] == 202), 'milestone_unique'] = 163
raw_data.loc[(raw_data['milestone'] == 166) | (raw_data['milestone'] == 204) | (raw_data['milestone'] == 241), 'milestone_unique'] = 164
raw_data.loc[(raw_data['milestone'] == 568) | (raw_data['milestone'] == 606) | (raw_data['milestone'] == 643) | (raw_data['milestone'] == 681), 'milestone_unique'] = 165
raw_data.loc[(raw_data['milestone'] == 167), 'milestone_unique'] = 166
raw_data.loc[(raw_data['milestone'] == 168) | (raw_data['milestone'] == 205) | (raw_data['milestone'] == 242), 'milestone_unique'] = 167
raw_data.loc[(raw_data['milestone'] == 312) | (raw_data['milestone'] == 350) | (raw_data['milestone'] == 388), 'milestone_unique'] = 168
raw_data.loc[(raw_data['milestone'] == 72) | (raw_data['milestone'] == 108) | (raw_data['milestone'] == 146), 'milestone_unique'] = 169
raw_data.loc[(raw_data['milestone'] == 30) | (raw_data['milestone'] == 69) | (raw_data['milestone'] == 105),'milestone_unique'] = 170
raw_data.loc[(raw_data['milestone'] == 25) | (raw_data['milestone'] == 65), 'milestone_unique'] = 171
raw_data.loc[(raw_data['milestone'] == 230) | (raw_data['milestone'] == 269) | (raw_data['milestone'] == 306), 'milestone_unique'] = 172
raw_data.loc[(raw_data['milestone'] == 31) | (raw_data['milestone'] == 70) | (raw_data['milestone'] == 106) | (raw_data['milestone'] == 411) | (raw_data['milestone'] == 449), 'milestone_unique'] = 173
raw_data.loc[(raw_data['milestone'] == 191) | (raw_data['milestone'] == 227) | (raw_data['milestone'] == 266), 'milestone_unique'] = 174
raw_data.loc[(raw_data['milestone'] == 272) | (raw_data['milestone'] == 309) | (raw_data['milestone'] == 347) | (raw_data['milestone'] == 385), 'milestone_unique'] = 175
raw_data.loc[(raw_data['milestone'] == 471) | (raw_data['milestone'] == 508) | (raw_data['milestone'] == 546) | (raw_data['milestone'] == 585), 'milestone_unique'] = 176
raw_data.loc[(raw_data['milestone'] == 152) | (raw_data['milestone'] == 190) | (raw_data['milestone'] == 226) | (raw_data['milestone'] == 265), 'milestone_unique'] = 177
raw_data.loc[(raw_data['milestone'] == 592) | (raw_data['milestone'] == 628) | (raw_data['milestone'] == 667), 'milestone_unique'] = 178
raw_data.loc[(raw_data['milestone'] == 509) | (raw_data['milestone'] == 548) | (raw_data['milestone'] == 587), 'milestone_unique'] = 179
raw_data.loc[(raw_data['milestone'] == 672) | (raw_data['milestone'] == 711) | (raw_data['milestone'] == 750), 'milestone_unique'] = 180
raw_data.loc[(raw_data['milestone'] == 791), 'milestone_unique'] = 181
raw_data.loc[(raw_data['milestone'] == 631) | (raw_data['milestone'] == 670) | (raw_data['milestone'] == 707) | (raw_data['milestone'] == 746) | (raw_data['milestone'] == 786), 'milestone_unique'] = 182
raw_data.loc[(raw_data['milestone'] == 472) | (raw_data['milestone'] == 510) | (raw_data['milestone'] == 549) | (raw_data['milestone'] == 588), 'milestone_unique'] = 183
raw_data.loc[(raw_data['milestone'] == 792), 'milestone_unique'] = 184
raw_data.loc[(raw_data['milestone'] == 552) | (raw_data['milestone'] == 591) | (raw_data['milestone'] == 627) | (raw_data['milestone'] == 666), 'milestone_unique'] = 185
raw_data.loc[(raw_data['milestone'] == 629) | (raw_data['milestone'] == 668) | (raw_data['milestone'] == 705), 'milestone_unique'] = 186
raw_data.loc[(raw_data['milestone'] == 310) | (raw_data['milestone'] == 348) | (raw_data['milestone'] == 386) | (raw_data['milestone'] == 425), 'milestone_unique'] = 187
raw_data.loc[(raw_data['milestone'] == 470) | (raw_data['milestone'] == 507) | (raw_data['milestone'] == 545), 'milestone_unique'] = 188
raw_data.loc[(raw_data['milestone'] == 751) | (raw_data['milestone'] == 789), 'milestone_unique'] = 189
raw_data.loc[(raw_data['milestone'] == 427), 'milestone_unique'] = 190
raw_data.loc[(raw_data['milestone'] == 547) | (raw_data['milestone'] == 586), 'milestone_unique'] = 191
raw_data.loc[(raw_data['milestone'] == 351) | (raw_data['milestone'] == 389) | (raw_data['milestone'] == 428), 'milestone_unique'] = 192
raw_data.loc[(raw_data['milestone'] == 465), 'milestone_unique'] = 193
raw_data.loc[(raw_data['milestone'] == 352) | (raw_data['milestone'] == 390) | (raw_data['milestone'] == 429) | (raw_data['milestone'] == 466), 'milestone_unique'] = 194
raw_data.loc[(raw_data['milestone'] == 632) | (raw_data['milestone'] == 671) | (raw_data['milestone'] == 708) | (raw_data['milestone'] == 747) | (raw_data['milestone'] == 787), 'milestone_unique'] = 195
raw_data.loc[(raw_data['milestone'] == 109) | (raw_data['milestone'] == 147) | (raw_data['milestone'] == 185), 'milestone_unique'] = 196
raw_data.loc[(raw_data['milestone'] == 112) | (raw_data['milestone'] == 150) | (raw_data['milestone'] == 189) | (raw_data['milestone'] == 225), 'milestone_unique'] = 197
raw_data.loc[(raw_data['milestone'] == 29) | (raw_data['milestone'] == 68), 'milestone_unique'] = 198
raw_data.loc[(raw_data['milestone'] == 709) | (raw_data['milestone'] == 748) | (raw_data['milestone'] == 788), 'milestone_unique'] = 199
raw_data.loc[(raw_data['milestone'] == 192) | (raw_data['milestone'] == 229) | (raw_data['milestone'] == 268) | (raw_data['milestone'] == 305), 'milestone_unique'] = 200
raw_data.loc[(raw_data['milestone'] == 392) | (raw_data['milestone'] == 431) | (raw_data['milestone'] == 468) | (raw_data['milestone'] == 505), 'milestone_unique'] = 201
raw_data.loc[(raw_data['milestone'] == 26) | (raw_data['milestone'] == 66), 'milestone_unique'] = 202
raw_data.loc[(raw_data['milestone'] == 32) | (raw_data['milestone'] == 71) | (raw_data['milestone'] == 107) | (raw_data['milestone'] == 145), 'milestone_unique'] = 203
raw_data.loc[(raw_data['milestone'] == 231) | (raw_data['milestone'] == 270) | (raw_data['milestone'] == 307) | (raw_data['milestone'] == 345), 'milestone_unique'] = 204
raw_data.loc[(raw_data['milestone'] == 432) | (raw_data['milestone'] == 469) | (raw_data['milestone'] == 506), 'milestone_unique'] = 205
raw_data.loc[(raw_data['milestone'] == 110) | (raw_data['milestone'] == 148) | (raw_data['milestone'] == 186) | (raw_data['milestone'] == 228) | (raw_data['milestone'] == 267), 'milestone_unique'] = 206
raw_data.loc[(raw_data['milestone'] == 511) | (raw_data['milestone'] == 550), 'milestone_unique'] = 207
raw_data.loc[(raw_data['milestone'] == 589) | (raw_data['milestone'] == 625), 'milestone_unique'] = 208
raw_data.loc[(raw_data['milestone'] == 27) | (raw_data['milestone'] == 67), 'milestone_unique'] = 209
raw_data.loc[(raw_data['milestone'] == 151) | (raw_data['milestone'] == 188), 'milestone_unique'] = 210
raw_data.loc[(raw_data['milestone'] == 590) | (raw_data['milestone'] == 626) | (raw_data['milestone'] == 665), 'milestone_unique'] = 211
raw_data.loc[(raw_data['milestone'] == 232) | (raw_data['milestone'] == 271) | (raw_data['milestone'] == 308) | (raw_data['milestone'] == 346), 'milestone_unique'] = 212
raw_data.loc[(raw_data['milestone'] == 710) | (raw_data['milestone'] == 749), 'milestone_unique'] = 213
raw_data.loc[(raw_data['milestone'] == 391) | (raw_data['milestone'] == 430) | (raw_data['milestone'] == 467), 'milestone_unique'] = 214
raw_data.loc[(raw_data['milestone'] == 712) | (raw_data['milestone'] == 752) | (raw_data['milestone'] == 790), 'milestone_unique'] = 215
raw_data.loc[(raw_data['milestone'] == 111) | (raw_data['milestone'] == 149) | (raw_data['milestone'] == 187), 'milestone_unique'] = 216
raw_data.loc[(raw_data['milestone'] == 28), 'milestone_unique'] = 217
raw_data.loc[(raw_data['milestone'] == 311) | (raw_data['milestone'] == 349) | (raw_data['milestone'] == 387) | (raw_data['milestone'] == 426), 'milestone_unique'] = 218
raw_data.loc[(raw_data['milestone'] == 630) | (raw_data['milestone'] == 669) | (raw_data['milestone'] == 706) | (raw_data['milestone'] == 745) | (raw_data['milestone'] == 785), 'milestone_unique'] = 219
raw_data.loc[(raw_data['milestone'] == 512) | (raw_data['milestone'] == 551), 'milestone_unique'] = 220
#raw_data.loc[(xls['milestone'] == ), 'milestone_unique'] = 221
raw_data.loc[(raw_data['milestone'] == 702) | (raw_data['milestone'] == 740), 'milestone_unique'] = 222
raw_data.loc[(raw_data['milestone'] == 743) | (raw_data['milestone'] == 779), 'milestone_unique'] = 223
raw_data.loc[(raw_data['milestone'] == 781), 'milestone_unique'] = 224
raw_data.loc[(raw_data['milestone'] == 544) | (raw_data['milestone'] == 581) | (raw_data['milestone'] == 618) | (raw_data['milestone'] == 658), 'milestone_unique'] = 225
raw_data.loc[(raw_data['milestone'] == 543) | (raw_data['milestone'] == 580) | (raw_data['milestone'] == 617) | (raw_data['milestone'] == 657), 'milestone_unique'] = 226
raw_data.loc[(raw_data['milestone'] == 59), 'milestone_unique'] = 227
raw_data.loc[(raw_data['milestone'] == 264) | (raw_data['milestone'] == 302) | (raw_data['milestone'] == 341) | (raw_data['milestone'] == 379) | (raw_data['milestone'] == 417), 'milestone_unique'] = 228
raw_data.loc[(raw_data['milestone'] == 63) | (raw_data['milestone'] == 100) | (raw_data['milestone'] == 138) | (raw_data['milestone'] == 177), 'milestone_unique'] = 229
raw_data.loc[(raw_data['milestone'] == 18), 'milestone_unique'] = 230
raw_data.loc[(raw_data['milestone'] == 184) | (raw_data['milestone'] == 222) | (raw_data['milestone'] == 259) | (raw_data['milestone'] == 297) | (raw_data['milestone'] ==337), 'milestone_unique'] = 231
raw_data.loc[(raw_data['milestone'] == 582) | (raw_data['milestone'] == 619) | (raw_data['milestone'] == 659), 'milestone_unique'] = 232
raw_data.loc[(raw_data['milestone'] == 583) | (raw_data['milestone'] == 620), 'milestone_unique'] = 233
raw_data.loc[(raw_data['milestone'] == 784), 'milestone_unique'] = 234
raw_data.loc[(raw_data['milestone'] == 383), 'milestone_unique'] = 235
raw_data.loc[(raw_data['milestone'] == 223) | (raw_data['milestone'] == 260) | (raw_data['milestone'] == 298) | (raw_data['milestone'] == 338), 'milestone_unique'] = 236
raw_data.loc[(raw_data['milestone'] == 422) | (raw_data['milestone'] == 460),'milestone_unique'] = 237
raw_data.loc[(raw_data['milestone'] == 303) | (raw_data['milestone'] == 342) | (raw_data['milestone'] == 380) | (raw_data['milestone'] == 418), 'milestone_unique'] = 238
raw_data.loc[(raw_data['milestone'] == 700) | (raw_data['milestone'] == 738), 'milestone_unique'] = 239
raw_data.loc[(raw_data['milestone'] == 343) | (raw_data['milestone'] == 381) | (raw_data['milestone'] == 420) | (raw_data['milestone'] == 458), 'milestone_unique'] = 240
raw_data.loc[(raw_data['milestone'] == 424) | (raw_data['milestone'] == 464) | (raw_data['milestone'] == 500), 'milestone_unique'] = 241
raw_data.loc[(raw_data['milestone'] == 263) | (raw_data['milestone'] == 301) | (raw_data['milestone'] == 339) | (raw_data['milestone'] == 377), 'milestone_unique'] = 242
raw_data.loc[(raw_data['milestone'] == 501), 'milestone_unique'] = 243
raw_data.loc[(raw_data['milestone'] == 22) | (raw_data['milestone'] == 60) | (raw_data['milestone'] == 97), 'milestone_unique'] = 244
raw_data.loc[(raw_data['milestone'] == 21), 'milestone_unique'] = 245
raw_data.loc[(raw_data['milestone'] == 64) | (raw_data['milestone'] == 101) | (raw_data['milestone'] == 139) | (raw_data['milestone'] == 178), 'milestone_unique'] = 246
raw_data.loc[(raw_data['milestone'] == 384) | (raw_data['milestone'] == 423) | (raw_data['milestone'] == 461) | (raw_data['milestone'] == 498), 'milestone_unique'] = 247
raw_data.loc[(raw_data['milestone'] == 621) | (raw_data['milestone'] == 660), 'milestone_unique'] = 248
raw_data.loc[(raw_data['milestone'] == 344) | (raw_data['milestone'] == 382), 'milestone_unique'] = 249
raw_data.loc[(raw_data['milestone'] == 421) | (raw_data['milestone'] == 459) | (raw_data['milestone'] == 497), 'milestone_unique'] = 250
raw_data.loc[(raw_data['milestone'] == 584) | (raw_data['milestone'] == 623) | (raw_data['milestone'] == 662), 'milestone_unique'] = 251
raw_data.loc[(raw_data['milestone'] == 102) | (raw_data['milestone'] == 140) | (raw_data['milestone'] == 179) | (raw_data['milestone'] == 217), 'milestone_unique'] = 252
raw_data.loc[(raw_data['milestone'] == 542) | (raw_data['milestone'] == 579), 'milestone_unique'] = 253
raw_data.loc[(raw_data['milestone'] == 17), 'milestone_unique'] = 254
raw_data.loc[(raw_data['milestone'] == 624) | (raw_data['milestone'] == 663) | (raw_data['milestone'] == 698), 'milestone_unique'] = 255
raw_data.loc[(raw_data['milestone'] == 103) | (raw_data['milestone'] == 141) | (raw_data['milestone'] == 180) | (raw_data['milestone'] == 218), 'milestone_unique'] = 256
raw_data.loc[(raw_data['milestone'] == 144) | (raw_data['milestone'] == 183) | (raw_data['milestone'] == 221) | (raw_data['milestone'] == 258), 'milestone_unique'] = 257
raw_data.loc[(raw_data['milestone'] == 224) | (raw_data['milestone'] == 261) | (raw_data['milestone'] == 299), 'milestone_unique'] = 258
raw_data.loc[(raw_data['milestone'] == 622) | (raw_data['milestone'] == 661) | (raw_data['milestone'] == 697), 'milestone_unique'] = 259
raw_data.loc[(raw_data['milestone'] == 503) | (raw_data['milestone'] == 539), 'milestone_unique'] = 260
raw_data.loc[(raw_data['milestone'] == 19) | (raw_data['milestone'] == 57) | (raw_data['milestone'] == 701) | (raw_data['milestone'] == 739), 'milestone_unique'] = 261
raw_data.loc[(raw_data['milestone'] == 783), 'milestone_unique'] = 262
raw_data.loc[(raw_data['milestone'] == 463) | (raw_data['milestone'] == 499) | (raw_data['milestone'] == 537), 'milestone_unique'] = 263
raw_data.loc[(raw_data['milestone'] == 504) | (raw_data['milestone'] == 540) | (raw_data['milestone'] == 577), 'milestone_unique'] = 264
raw_data.loc[(raw_data['milestone'] == 704) | (raw_data['milestone'] == 742) | (raw_data['milestone'] == 778), 'milestone_unique'] = 265
raw_data.loc[(raw_data['milestone'] == 744) | (raw_data['milestone'] == 780), 'milestone_unique'] = 266
raw_data.loc[(raw_data['milestone'] == 20) | (raw_data['milestone'] == 58), 'milestone_unique'] = 267
raw_data.loc[(raw_data['milestone'] == 541) | (raw_data['milestone'] == 578), 'milestone_unique'] = 268
raw_data.loc[(raw_data['milestone'] == 703) | (raw_data['milestone'] == 741) | (raw_data['milestone'] == 777), 'milestone_unique'] = 269
raw_data.loc[(raw_data['milestone'] == 664) | (raw_data['milestone'] == 699) | (raw_data['milestone'] == 737), 'milestone_unique'] = 270
raw_data.loc[(raw_data['milestone'] == 143) | (raw_data['milestone'] == 182) | (raw_data['milestone'] == 220) | (raw_data['milestone'] == 257), 'milestone_unique'] = 271
raw_data.loc[(raw_data['milestone'] == 104) | (raw_data['milestone'] == 142) | (raw_data['milestone'] == 181) | (raw_data['milestone'] == 219), 'milestone_unique'] = 272
raw_data.loc[(raw_data['milestone'] == 23) | (raw_data['milestone'] == 61) | (raw_data['milestone'] == 98), 'milestone_unique'] = 273
raw_data.loc[(raw_data['milestone'] == 419) | (raw_data['milestone'] == 457), 'milestone_unique'] = 274
raw_data.loc[(raw_data['milestone'] == 304), 'milestone_unique'] = 275
raw_data.loc[(raw_data['milestone'] == 340) | (raw_data['milestone'] == 378), 'milestone_unique'] = 276
raw_data.loc[(raw_data['milestone'] == 262) | (raw_data['milestone'] == 300), 'milestone_unique'] = 277
raw_data.loc[(raw_data['milestone'] == 24) | (raw_data['milestone'] == 62) | (raw_data['milestone'] == 99) | (raw_data['milestone'] == 137), 'milestone_unique'] = 278
raw_data.loc[(raw_data['milestone'] == 502) | (raw_data['milestone'] == 538), 'milestone_unique'] = 279
raw_data.loc[(raw_data['milestone'] == 462), 'milestone_unique'] = 280
raw_data.loc[(raw_data['milestone'] == 782), 'milestone_unique'] = 281
#print(raw_data)


# done_day_after_birth (생후일수) 지정해서 분석할 수 있도록 하는 기능

a=int(input("==========done_day_after_start_date=========="))
b=int(input("==========done_day_after_due_date=========="))



condition_1=raw_data['done_day_after_birth']>=a
condition_2=raw_data['done_day_after_birth']<=b
sub_df=raw_data[condition_1 & condition_2]

print(sub_df)
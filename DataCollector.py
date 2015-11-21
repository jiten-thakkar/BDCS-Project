import datetime
import os
import time
import pickle

import sys

import stockretriever

stockSymbols = ["AAL","AAMC","AAN","AAOI","AAON","AAPL","AAP","AAT","AAWW","AA","ABAX","ABBV","ABCB","ABCO","ABC","ABG","ABMD","ABM","ABT","ACAD","ACAS","ACAT","ACCO","ACC","ACET","ACE","ACFN","ACGL","ACHC","ACHN","ACIW","ACI","ACLS","ACM","ACN","ACOR","ACRE","ACRX","ACTG","ACW","ACXM","ADBE","ADC","ADI","ADMS","ADM","ADP","ADSK","ADS","ADTN","ADT","ADUS","AEC","AEE","AEGN","AEGR","AEIS","AEL","AEO","AEPI","AEP","AERI","AES","AET","AE","AFAM","AFFX","AFG","AFH","AFL","AFOP","AFSI","AF","AGCO","AGEN","AGII","AGIO","AGM","AGNC","AGN","AGO","AGTC","AGX","AGYS","AHC","AHH","AHL","AHP","AHS","AHT","AIG","AIMC","AINV","AIN","AIQ","AIRM","AIR","AIT","AIV","AIZ","AI","AJG","AKAM","AKAO","AKBA","AKRX","AKR","AKS","ALB","ALCO","ALDR","ALEX","ALE","ALGN","ALGT","ALG","ALIM","ALJ","ALKS","ALK","ALLE","ALL","ALNY","ALOG","ALR","ALSN","ALTR","ALXN","ALX","AL","AMAG","AMAT","AMBA","AMBC","AMBR","AMCC","AMCX","AMC","AMD","AMED","AME","AMGN","AMG","AMKR","AMNB","AMPE","AMP","AMRC","AMRI","AMRS","AMSC","AMSF","AMSG","AMSWA","AMTD","AMTG","AMT","AMWD","AMZN","ANAC","ANAD","ANAT","ANCX","ANDE","ANF","ANGI","ANGO","ANH","ANIK","ANIP","ANN","ANR","ANSS","ANTM","AN","AOI","AON","AOSL","AOS","APAM","APA","APC","APD","APEI","APH","APOG","APOL","APP","AP","ARAY","ARCB","ARCC","ARCW","ARC","AREX","ARE","ARG","ARIA","ARII","ARI","ARNA","AROW","ARO","ARPI","ARQL","ARRS","ARRY","ARR","ARTNA","ARWR","ARW","ASCMA","ASC","ASEI","ASGN","ASH","ASNA","ASPS","ASTE","ATEC","ATEN","ATHN","ATLO","ATML","ATNI","ATNM","ATNY","ATO","ATRC","ATRI","ATRO","ATRS","ATR","ATSG","ATU","ATVI","ATW","AT","AVAV","AVA","AVB","AVD","AVEO","AVGO","AVG","AVHI","AVID","AVNW","AVT","AVX","AVY","AWAY","AWH","AWI","AWK","AWR","AXAS","AXDX","AXE","AXLL","AXL","AXP","AXS","AYI","AYR","AZO","AZPN","AZZ","A","BABY","BAC","BAGR","BAH","BALT","BANC","BANF","BANR","BAS","BAX","BA","BBBY","BBCN","BBGI","BBG","BBOX","BBRG","BBSI","BBT","BBW","BBX","BBY","BCC","BCEI","BCOR","BCOV","BCO","BCPC","BCRX","BCR","BC","BDBD","BDC","BDE","BDGE","BDN","BDSI","BDX","BEAT","BEAV","BEBE","BECN","BEE","BELFB","BEN","BERY","BF_B","BFAM","BFIN","BFS","BGCP","BGC","BGFV","BGG","BGS","BG","BHB","BHE","BHI","BHLB","BH","BIDU","BID","BIG","BIIB","BIOL","BIOS","BIO","BJRI","BKCC","BKD","BKE","BKH","BKMU","BKS","BKU","BK","BLDR","BLKB","BLK","BLL","BLMN","BLOX","BLT","BLUE","BLX","BMI","BMRC","BMRN","BMR","BMS","BMTC","BMY","BNCL","BNCN","BNFT","BOBE","BOFI","BOH","BOKF","BONT","BOOM","BPFH","BPI","BPOP","BPTH","BP","BRCD","BRCM","BRC","BREW","BRK_A","BRKL","BRKR","BRKS","BRLI","BRO","BRSS","BRS","BRT","BR","BSET","BSFT","BSRR","BSTC","BSX","BTH","BTU","BTX","BURL","BUSE","BV","BWA","BWINB","BWLD","BXC","BXLT","BXP","BXS","BYD","BZH","B","CAB","CACB","CACC","CACI","CACQ","CAC","CAG","CAH","CAKE","CALD","CALL","CALM","CALX","CAMP","CAM","CAP","CARA","CARB","CAR","CASH","CASS","CASY","CAS","CATM","CATO","CATY","CAT","CAVM","CA","CBB","CBF","CBG","CBI","CBK","CBL","CBM","CBOE","CBPX","CBRL","CBR","CBSH","CBS","CBT","CBU","CBZ","CB","CCBG","CCC","CCE","CCF","CCG","CCI","CCK","CCL","CCMP","CCNE","CCOI","CCO","CCRN","CCXI","CDE","CDI","CDNS","CDR","CEB","CECE","CECO","CELG","CEMP","CENTA","CENX","CERN","CERS","CETV","CEVA","CE","CFFI","CFFN","CFI","CFNB","CFNL","CFR","CFX","CF","CGI","CGNX","CHCO","CHDN","CHD","CHEF","CHE","CHFC","CHFN","CHGG","CHH","CHKP","CHK","CHMG","CHMT","CHRW","CHSP","CHS","CHTR","CHUY","CIA","CIDM","CIEN","CIE","CIFC","CIM","CINF","CIR","CIT","CIX","CI","CJES","CKEC","CKH","CKP","CLCT","CLC","CLDT","CLDX","CLD","CLFD","CLF","CLGX","CLH","CLI","CLMS","CLNE","CLNY","CLR","CLUB","CLVS","CLW","CLX","CL","CMA","CMCO","CMCSA","CMC","CME","CMG","CMI","CMLS","CMN","CMO","CMP","CMRX","CMS","CMTL","CNA","CNBKA","CNC","CNK","CNL","CNMD","CNOB","CNO","CNP","CNSI","CNSL","CNS","CNW","CNX","COBZ","COB","COF","COG","COHR","COHU","COH","COKE","COLB","COLM","COL","CONE","CONN","COO","COP","CORE","CORR","CORT","COR","COST","COUP","COVS","COWN","CPA","CPB","CPE","CPF","CPGX","CPHD","CPK","CPLA","CPN","CPRT","CPSI","CPSS","CPST","CPS","CPT","CRAI","CRAY","CRCM","CRD_B","CREE","CRIS","CRI","CRK","CRL","CRMT","CRM","CROX","CRR","CRS","CRUS","CRVL","CRWN","CRY","CRZO","CR","CSBK","CSCD","CSCO","CSC","CSFL","CSGP","CSGS","CSG","CSH","CSII","CSLT","CSL","CSOD","CSS","CST","CSU","CSV","CSWC","CSX","CTAS","CTBI","CTB","CTCT","CTG","CTIC","CTL","CTO","CTRE","CTRL","CTRN","CTRX","CTSH","CTS","CTT","CTWS","CTXS","CUBE","CUBI","CUB","CUDA","CUI","CUNB","CUR","CUTR","CUZ","CVA","CVBF","CVCO","CVC","CVEO","CVGI","CVGW","CVG","CVI","CVLT","CVO","CVS","CVT","CVX","CWCO","CWEI","CWST","CWT","CW","CXO","CXW","CYBX","CYH","CYNI","CYNO","CYN","CYS","CYTK","CYTR","CYTX","CYT","CY","CZNC","CZR","C","DAKT","DAL","DAN","DAR","DATA","DAVE","DBD","DCI","DCOM","DCO","DCT","DDD","DDR","DDS","DD","DECK","DEI","DEL","DENN","DEPO","DEST","DE","DFRG","DFS","DFT","DF","DGAS","DGICA","DGII","DGI","DGX","DG","DHIL","DHI","DHR","DHT","DHX","DIN","DIOD","DISCA","DISCK","DISH","DIS","DJCO","DKS","DK","DLB","DLPH","DLR","DLTR","DLX","DMD","DMND","DMRC","DNB","DNKN","DNR","DOC","DOOR","DORM","DOV","DOW","DOX","DO","DPS","DPZ","DRE","DRH","DRII","DRI","DRNA","DRQ","DSCI","DSPG","DST","DSW","DTE","DTLK","DTSI","DTV","DUK","DVAX","DVA","DVN","DV","DWA","DWRE","DWSN","DW","DXCM","DXLG","DXM","DXPE","DXYN","DX","DYAX","DYN","DY","D","EAC","EAT","EA","EBAY","EBF","EBIO","EBIX","EBSB","EBS","EBTC","ECHO","ECL","ECOL","ECOM","ECPG","ECYT","EDE","EDR","ED","EEFT","EE","EFII","EFSC","EFX","EGAN","EGBN","EGHT","EGLT","EGL","EGN","EGOV","EGP","EGY","EHTH","EIGI","EIG","EIX","ELGX","ELLI","ELNK","ELRC","ELS","ELY","EL","EMCI","EMC","EME","EMN","EMR","ENDP","ENH","ENOC","ENPH","ENR","ENSG","ENS","ENTA","ENTG","ENT","ENV","ENZN","ENZ","EOG","EOX","EPAM","EPAY","EPIQ","EPM","EPR","EPZM","EQIX","EQR","EQT","EQY","ERA","ERIE","ERII","EROS","ESCA","ESE","ESGR","ESIO","ESI","ESL","ESNT","ESPR","ESRT","ESRX","ESSA","ESS","ESV","ES","ETFC","ETH","ETM","ETN","ETR","EVC","EVDY","EVER","EVR","EVTC","EV","EWBC","EW","EXAC","EXAM","EXAR","EXAS","EXC","EXEL","EXH","EXLS","EXL","EXPD","EXPE","EXPO","EXPR","EXP","EXR","EXTR","EXXI","EZPW","FAF","FANG","FARM","FARO","FAST","FBC","FBHS","FBIZ","FBNC","FBNK","FBP","FBRC","FB","FCBC","FCE_A","FCEL","FCFS","FCF","FCH","FCNCA","FCN","FCSC","FCS","FCX","FC","FDEF","FDML","FDP","FDS","FDUS","FDX","FEIC","FELE","FET","FE","FFBC","FFG","FFIC","FFIN","FFIV","FFKT","FFNW","FF","FGL","FHCO","FHN","FIBK","FICO","FII","FINL","FISI","FISV","FIS","FITB","FIVE","FIVN","FIX","FIZZ","FLDM","FLIC","FLIR","FLO","FLR","FLS","FLTX","FLT","FLWS","FLXN","FLXS","FL","FMBI","FMC","FMD","FMER","FMI","FNB","FNFG","FNF","FNGN","FNHC","FNLC","FNSR","FN","FOE","FOLD","FORM","FORR","FOR","FOSL","FOXA","FOXF","FOX","FPO","FPRX","FRAN","FRBK","FRC","FRED","FRGI","FRME","FRM","FRO","FRP","FRSH","FRT","FR","FSC","FSGI","FSLR","FSL","FSP","FSS","FSTR","FSYS","FTD","FTI","FTK","FTNT","FTR","FUEL","FULT","FUL","FUR","FVE","FWM","FWRD","FXCB","FXCM","FXEN","F","GABC","GAIA","GAIN","GALE","GALT","GARS","GAS","GBCI","GBDC","GBLI","GBL","GBNK","GBX","GB","GCAP","GCA","GCO","GDOT","GDP","GD","GEF","GEOS","GEO","GERN","GES","GE","GFF","GFN","GGG","GGP","GHC","GHDX","GHL","GHM","GIFI","GIII","GILD","GIMO","GIS","GK","GLAD","GLDD","GLF","GLNG","GLOG","GLPW","GLRE","GLRI","GLT","GLUU","GLW","GMAN","GMCR","GMED","GME","GMO","GMT","GM","GNCA","GNCMA","GNC","GNE","GNMK","GNRC","GNTX","GNW","GOGO","GOLD","GOOD","GOOGL","GOOG","GORO","GOV","GPC","GPI","GPK","GPN","GPOR","GPRE","GPS","GPT","GPX","GRA","GRC","GRIF","GRMN","GRPN","GRUB","GSAT","GSBC","GSIG","GSIT","GSM","GSOL","GST","GSVC","GS","GTI","GTLS","GTN","GTS","GTT","GTXI","GTY","GT","GUID","GVA","GWRE","GWR","GWW","GXP","G","HAE","HAFC","HAIN","HALL","HALO","HAL","HAR","HASI","HAS","HAWK","HAYN","HA","HBAN","HBCP","HBHC","HBIO","HBI","HBNC","HCA","HCBK","HCCI","HCC","HCI","HCKT","HCN","HCOM","HCP","HCSG","HDNG","HD","HEAR","HEES","HEI","HELE","HELI","HEOP","HERO","HES","HE","HFC","HFWA","HF","HGG","HGR","HHC","HHS","HIBB","HIFS","HIG","HIIQ","HII","HILL","HIL","HIVE","HIW","HI","HK","HLF","HLIT","HLS","HLX","HL","HME","HMHC","HMN","HMPR","HMST","HMSY","HMTV","HNH","HNI","HNRG","HNR","HNT","HOFT","HOG","HOLX","HOMB","HON","HOS","HOT","HOV","HPP","HPQ","HPT","HPY","HP","HRB","HRC","HRG","HRL","HRS","HRTG","HRTX","HRZN","HR","HSC","HSIC","HSII","HSNI","HSP","HSTM","HST","HSY","HTA","HTBI","HTBK","HTCH","HTGC","HTH","HTLD","HTLF","HTS","HTWR","HTZ","HT","HUB_B","HUBG","HUM","HUN","HURC","HURN","HVT","HWAY","HWCC","HWKN","HW","HXL","HY","HZNP","HZO","H","IACI","IART","IBCP","IBKC","IBKR","IBM","IBOC","IBP","IBTX","ICE","ICFI","ICON","ICPT","ICUI","IDA","IDCC","IDRA","IDTI","IDT","IDXX","IEX","IFF","IFT","IGT","IG","IHC","IHS","IIIN","III","IILG","IIVI","ILMN","IL","IMGN","IMI","IMKTA","IMMR","IMMU","IMN","IMPV","IM","INAP","INCY","INDB","INFA","INFI","INFN","INGN","INGR","ININ","INN","INO","INSM","INSY","INTC","INTL","INTU","INTX","INT","INVN","INWK","IOSP","IO","IPAR","IPCC","IPCM","IPGP","IPG","IPHI","IPHS","IPI","IPXL","IP","IQNT","IRBT","IRC","IRDM","IRET","IRG","IRM","IRWD","IR","ISBC","ISCA","ISH","ISIL","ISIS","ISLE","ISRG","ISRL","ISSC","ISSI","ITCI","ITC","ITG","ITIC","ITRI","ITT","ITW","IT","IVAC","IVC","IVR","IVZ","IXYS","I","JACK","JAH","JAKK","JBHT","JBLU","JBL","JBSS","JBT","JCI","JCOM","JCP","JDSU","JEC","JGW","JIVE","JJSF","JKHY","JLL","JMBA","JNJ","JNPR","JNS","JOE","JONE","JOUT","JOY","JPM","JW_A","JWN","KAI","KALU","KAMN","KAR","KBH","KBR","KCG","KCLI","KEG","KELYA","KEM","KERX","KEX","KEYW","KEY","KFRC","KFY","KIM","KIN","KIRK","KKD","KLAC","KMB","KMG","KMI","KMPR","KMT","KMX","KND","KNL","KNX","KODK","KOPN","KOP","KORS","KOS","KO","KPTI","KRA","KRC","KRG","KRNY","KRO","KR","KSS","KSU","KS","KTOS","KTWO","KVHI","KWR","KW","KYTH","K","LABL","LADR","LAD","LAMR","LANC","LAYN","LAZ","LBAI","LBMH","LBTYA","LBY","LB","LCI","LCNB","LCUT","LDL","LDOS","LDRH","LDR","LEAF","LEA","LECO","LEE","LEG","LEN","LE","LFUS","LFVN","LF","LGF","LGIH","LGND","LG","LHCG","LHO","LH","LII","LINC","LION","LIOX","LKFN","LKQ","LLL","LLNW","LLTC","LLY","LL","LMCA","LMIA","LMNR","LMNX","LMOS","LMT","LM","LNCE","LNC","LNDC","LNG","LNKD","LNN","LNT","LOCK","LOGM","LOPE","LORL","LOV","LOW","LPG","LPI","LPLA","LPNT","LPSN","LPX","LQDT","LQ","LRCX","LRN","LSCC","LSTR","LTC","LTS","LUB","LUK","LUV","LVLT","LVNTA","LVS","LWAY","LXFT","LXK","LXP","LXRX","LXU","LYB","LYTS","LYV","LZB","L","MACK","MAC","MAIN","MANH","MANT","MAN","MAR","MASI","MAS","MATW","MATX","MAT","MA","MBFI","MBII","MBI","MBRG","MBUU","MBVT","MBWM","MCBC","MCC","MCD","MCF","MCGC","MCHP","MCHX","MCK","MCO","MCRI","MCRL","MCS","MCY","MC","MDAS","MDCA","MDCO","MDC","MDLZ","MDP","MDRX","MDR","MDSO","MDT","MDU","MDVN","MDXG","MD","MED","MEG","MEIP","MEI","MENT","METR","MET","MFA","MFLX","MFRM","MGEE","MGI","MGLN","MGM","MGNX","MGRC","MG","MHFI","MHGC","MHK","MHLD","MHO","MHR","MIDD","MILL","MIL","MIND","MINI","MITK","MITT","MJN","MKC","MKL","MKSI","MKTO","MKTX","MLAB","MLHR","MLI","MLM","MLNK","MLR","MMC","MMI","MMM","MMSI","MMS","MM","MNI","MNKD","MNK","MNRO","MNR","MNST","MNTA","MNTX","MN","MODN","MOD","MOFG","MOG_A","MOH","MON","MORN","MOSY","MOS","MOV","MO","MPAA","MPC","MPO","MPWR","MPW","MPX","MRCY","MRC","MRGE","MRH","MRIN","MRK","MRLN","MRO","MRTN","MRTX","MRVL","MSA","MSCC","MSCI","MSEX","MSFG","MSFT","MSG","MSI","MSL","MSM","MSO","MSTR","MS","MTB","MTDR","MTD","MTGE","MTG","MTH","MTN","MTOR","MTRN","MTRX","MTSC","MTSI","MTW","MTX","MTZ","MUR","MUSA","MU","MVC","MWA","MWW","MW","MXIM","MXL","MXWL","MYCC","MYE","MYGN","MYL","MYRG","M","NADL","NANO","NATH","NATI","NATL","NATR","NAT","NAVB","NAVG","NAVI","NAV","NBBC","NBHC","NBIX","NBL","NBTB","NCI","NCLH","NCMI","NCR","NCS","NC","NDAQ","NDLS","NDSN","NEE","NEM","NEOG","NEON","NEO","NES","NETE","NEU","NEWM","NEWP","NEWS","NE","NFBK","NFG","NFLX","NFX","NGHC","NGS","NGVC","NHC","NHI","NICK","NIHD","NILE","NI","NJR","NKE","NKSH","NKTR","NLNK","NLSN","NLS","NLY","NL","NMBL","NMFC","NMIH","NMRX","NM","NNA","NNBR","NNI","NNVC","NOC","NOG","NOR","NOV","NOW","NPBC","NPK","NPO","NPTN","NP","NRCIA","NRG","NRIM","NRZ","NR","NSC","NSIT","NSM","NSPH","NSP","NSR","NSTG","NTAP","NTCT","NTGR","NTK","NTLS","NTRI","NTRS","NUAN","NUE","NUS","NUTR","NUVA","NVAX","NVDA","NVEC","NVR","NWBI","NWBO","NWE","NWHM","NWLI","NWL","NWN","NWPX","NWSA","NWY","NXST","NXTM","NX","NYCB","NYLD","NYMT","NYNY","NYRT","NYT","N","OAS","OB","OCFC","OCLR","OCN","OCR","OC","ODC","ODFL","ODP","OFC","OFG","OFIX","OFLX","OGE","OGS","OGXI","OHI","OHRP","OII","OIS","OI","OKE","OKSB","OLBK","OLED","OLN","OLP","OMCL","OMC","OMED","OMER","OMEX","OME","OMG","OMI","OMN","ONB","ONE","ONTY","ONVO","OPB","OPHT","OPK","OPWR","OPY","ORA","ORBC","ORCL","OREX","ORIT","ORI","ORLY","ORM","ORN","OSIR","OSIS","OSK","OSTK","OSUR","OTTR","OUTR","OVAS","OVTI","OWW","OXFD","OXM","OXY","OZRK","O","PACB","PACW","PAG","PAHC","PANW","PATK","PAYC","PAYX","PAY","PBCT","PBF","PBH","PBI","PBPB","PBYI","PBY","PB","PCAR","PCBK","PCCC","PCG","PCH","PCLN","PCL","PCO","PCP","PCRX","PCTI","PCTY","PCYG","PCYO","PDCE","PDCO","PDFS","PDLI","PDM","PEBO","PEB","PEGA","PEGI","PEG","PEIX","PEI","PENN","PEP","PERI","PERY","PES","PETS","PETX","PE","PFBC","PFE","PFG","PFIE","PFIS","PFLT","PFMT","PFPT","PFSI","PFS","PF","PGC","PGEM","PGI","PGNX","PGR","PGTI","PG","PHH","PHIIK","PHMD","PHM","PHX","PH","PICO","PII","PIR","PJC","PKD","PKE","PKG","PKI","PKOH","PKY","PLAB","PLCE","PLCM","PLD","PLKI","PLL","PLMT","PLOW","PLPC","PLPM","PLT","PLUG","PLUS","PLXS","PMCS","PMC","PMFG","PMT","PM","PNC","PNFP","PNK","PNM","PNNT","PNRA","PNR","PNW","PNX","PNY","PODD","POL","POM","POOL","POR","POST","POWI","POWL","POWR","POZN","PPBI","PPC","PPG","PPHM","PPL","PPO","PPS","PQ","PRAA","PRA","PRE","PRFT","PRGO","PRGS","PRGX","PRIM","PRI","PRKR","PRK","PRLB","PROV","PRO","PRSC","PRTA","PRU","PRXL","PSA","PSB","PSEC","PSEM","PSIX","PSMT","PSTB","PSUN","PSX","PTCT","PTEN","PTIE","PTLA","PTSI","PTX","PVA","PVH","PVTB","PWOD","PWR","PXD","PX","PZG","PZN","PZZA","P","QADA","QCOM","QDEL","QGEN","QLGC","QLIK","QLTY","QLYS","QNST","QRHC","QRVO","QSII","QTM","QTS","QTWO","QUAD","QUIK","Q","RAD","RAIL","RAI","RARE","RAS","RATE","RAVN","RAX","RBCAA","RBCN","RBC","RCAP","RCII","RCL","RCPT","RDEN","RDI","RDNT","RDN","RECN","REGI","REGN","REG","REIS","REI","RELL","REMY","RENT","REN","RESI","RES","REV","REXI","REXR","REXX","REX","RE","RFP","RF","RGA","RGC","RGEN","RGLD","RGLS","RGR","RGS","RHI","RHP","RHT","RH","RIGL","RIG","RJET","RJF","RKUS","RLD","RLGY","RLI","RLJ","RLOC","RLYP","RL","RMAX","RMBS","RMD","RMTI","RM","RNDY","RNET","RNG","RNR","RNST","RNWK","ROCK","ROG","ROIAK","ROIC","ROK","ROLL","ROL","ROP","ROSE","ROST","ROVI","RPAI","RPM","RPRX","RPTP","RPT","RPXC","RP","RRC","RRD","RRGB","RRTS","RSE","RSG","RSO","RSPP","RSTI","RST","RSYS","RS","RTEC","RTIX","RTI","RTK","RTN","RTRX","RT","RUBI","RUSHA","RUTH","RVLT","RVNC","RWT","RXN","RYL","RYN","R","SAAS","SAFM","SAFT","SAH","SAIA","SAIC","SALE","SALM","SALT","SAMG","SAM","SANM","SASR","SATS","SAVE","SBAC","SBCF","SBGI","SBH","SBNY","SBRA","SBSI","SBUX","SBY","SB","SCAI","SCCO","SCG","SCHL","SCHN","SCHW","SCI","SCLN","SCL","SCMP","SCM","SCOR","SCSC","SCSS","SCS","SCTY","SCVL","SDRL","SD","SEAC","SEAS","SEB","SEE","SEIC","SEMG","SEM","SENEA","SE","SFBS","SFE","SFG","SFLY","SFL","SFNC","SFXE","SFY","SF","SGA","SGBK","SGEN","SGI","SGMO","SGMS","SGM","SGNT","SGYP","SGY","SHEN","SHLD","SHLM","SHLO","SHOO","SHOR","SHOS","SHO","SHW","SIAL","SIF","SIGI","SIGM","SIG","SIRI","SIRO","SIR","SIVB","SIX","SJI","SJM","SJW","SKT","SKUL","SKX","SKYW","SLAB","SLB","SLCA","SLGN","SLG","SLH","SLRC","SMCI","SMG","SMP","SMRT","SMTC","SM","SNAK","SNA","SNBC","SNCR","SNDK","SNHY","SNH","SNI","SNMX","SNOW","SNPS","SNSS","SNTA","SNV","SNX","SN","SONC","SONS","SON","SO","SPAR","SPA","SPB","SPDC","SPF","SPG","SPLK","SPLS","SPNC","SPNS","SPN","SPPI","SPRT","SPR","SPSC","SPTN","SPWH","SPWR","SPW","SP","SQBG","SQBK","SQI","SQNM","SRCE","SRCL","SRDX","SREV","SRE","SRI","SRPT","SSD","SSI","SSNC","SSNI","SSP","SSS","SSTK","SSYS","STAA","STAG","STAR","STBA","STBZ","STCK","STC","STE","STFC","STI","STJ","STLD","STL","STML","STMP","STNG","STNR","STRA","STRL","STRT","STRZA","STR","STT","STWD","STX","STZ","SUBK","SUI","SUNE","SUNS","SUN","SUPN","SUP","SUSQ","SVU","SVVC","SWAY","SWC","SWFT","SWHC","SWI","SWKS","SWK","SWM","SWN","SWSH","SWX","SXC","SXI","SXT","SYA","SYBT","SYKE","SYK","SYMC","SYNA","SYNT","SYRG","SYUT","SYX","SYY","SZMK","SZYM","S","TAHO","TAL","TAP","TASR","TAST","TAT","TAXI","TAX","TBBK","TBI","TBNK","TBPH","TCAP","TCBI","TCBK","TCB","TCO","TCPC","TCRD","TCS","TDC","TDG","TDS","TDW","TDY","TEAR","TECD","TECH","TEL","TEN","TER","TESO","TESS","TEX","TE","TFM","TFSL","TFX","TGH","TGI","TGNA","TGTX","TGT","TG","THC","THFF","THG","THLD","THOR","THO","THRM","THRX","THR","THS","TICC","TIF","TILE","TIME","TIPT","TISI","TIS","TITN","TIVO","TJX","TKR","TK","TLMR","TLYS","TMHC","TMH","TMK","TMO","TMP","TMUS","TNAV","TNC","TNDM","TNET","TNGO","TNK","TOL","TOWN","TOWR","TPC","TPH","TPLM","TPRE","TPX","TRAK","TRC","TREC","TREE","TREX","TRGP","TRGT","TRIP","TRIV","TRI","TRK","TRMB","TRMK","TRMR","TRNO","TRNX","TRN","TROW","TROX","TRR","TRST","TRS","TRUE","TRV","TRXC","TR","TSCO","TSC","TSLA","TSN","TSO","TSRA","TSRE","TSRO","TSS","TSYS","TTC","TTEC","TTEK","TTGT","TTI","TTMI","TTPH","TTS","TTWO","TUES","TUMI","TUP","TWC","TWER","TWIN","TWI","TWMC","TWOU","TWO","TWTR","TWX","TW","TXMD","TXN","TXRH","TXTR","TXT","TYC","TYL","TYPE","TZOO","T","UACL","UAL","UAM","UA","UBA","UBNK","UBNT","UBSH","UBSI","UCBI","UCFC","UCP","UCTT","UDR","UEC","UEIC","UFCS","UFI","UFPI","UFPT","UFS","UGI","UHAL","UHS","UHT","UIHC","UIL","UIS","ULTA","ULTI","ULTR","UMBF","UMH","UMPQ","UNFI","UNF","UNH","UNIS","UNM","UNP","UNTD","UNT","UNXL","UPIP","UPL","UPS","URBN","URG","URI","USAK","USAP","USB","USCR","USG","USLM","USMD","USM","USNA","USPH","UTEK","UTHR","UTIW","UTI","UTL","UTMD","UTX","UVE","UVSP","UVV","VAC","VAL","VAR","VASC","VCRA","VCYT","VC","VDSI","VECO","VFC","VGR","VG","VHC","VIAB","VICL","VICR","VIVO","VLGEA","VLO","VLY","VMC","VMEM","VMI","VMW","VNCE","VNDA","VNO","VNTV","VOD","VOXX","VOYA","VPG","VRA","VRNG","VRNS","VRNT","VRSK","VRSN","VRTS","VRTU","VRTX","VR","VSAR","VSAT","VSEC","VSH","VSI","VSTM","VTG","VTL","VTNR","VTR","VVC","VVI","VVUS","VZ","V","WABC","WAB","WAC","WAFD","WAGE","WAIR","WAL","WASH","WAT","WBA","WBC","WBMD","WBS","WCC","WCG","WCIC","WCN","WDAY","WDC","WDFC","WDR","WD","WEC","WEN","WERN","WETF","WEX","WEYS","WFC","WFD","WFM","WGL","WGO","WG","WHF","WHG","WHR","WIBC","WIFI","WINA","WIRE","WIX","WLB","WLH","WLK","WLL","WMAR","WMB","WMC","WMGI","WMK","WMT","WM","WNC","WNR","WOOF","WOR","WPP","WPX","WRB","WRES","WRE","WRI","WRLD","WR","WSBC","WSBF","WSFS","WSM","WSO","WSR","WSTC","WSTL","WST","WTBA","WTFC","WTI","WTM","WTR","WTS","WTW","WU","WWAV","WWD","WWE","WWWW","WWW","WYNN","WYN","WY","XCO","XCRA","XEC","XEL","XLNX","XLRN","XL","XNCR","XNPT","XOMA","XOM","XONE","XON","XOOM","XOXO","XPO","XRAY","XRM","XRX","XXIA","XXII","XYL","X","YDKN","YELP","YHOO","YORW","YRCW","YUME","YUM","Y","ZAGG","ZAZA","ZBH","ZBRA","ZEN","ZEUS","ZGNX","ZINC","ZION","ZIOP","ZIXI","ZLTQ","ZNGA","ZOES","ZQK","ZTS","ZUMZ","Z"]
FILE_PREFIX = "QUOTES"
EXT = ".txt"
# data = stockretriever.get_current_info("GOOG")
# print datetime.datetime.now().second
# def fetchAllQuotes():
total = len(stockSymbols)
# print str(sys.argv)
start = int(str(sys.argv[1]))
end = int(str(sys.argv[2]))
date = datetime.date.today()
epochTime = int(time.time())
# file = os.
try:
    data = stockretriever.get_current_info(stockSymbols[start:end])
    directory = FILE_PREFIX+"/"+str(date)
    if not os.path.exists(directory):
        os.makedirs(directory)
    pickle.dump(data, open(directory+"/"+str(epochTime)+EXT, "wb"))
except stockretriever.QueryError as e:
        print "Got error: " + str(e)
except KeyError as e:
        print "Got error: " + str(e)
except TypeError as e:
        print "Got error: " + str(e)
except Exception, err:
        print('ERROR: %sn' % str(err))

print str(datetime.datetime.now()) + " start= " + str(start) + " end= " + str(end)
# os.close(file)

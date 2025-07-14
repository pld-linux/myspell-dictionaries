# NOTE:
# - the dictionaries are usable for hunspell, openoffice (libreoffice), mozilla products
#   maybe we should package them all to /usr/share/dict or similiar
# - hyph_en_AU hyph_en_CA hyph_en_GB hyph_en_NZ hyph_en_US are all identical in ooo contrib
# - hyph_pt_BR and hyph_pt_PT contents are identical in ooo contrib

%define		rel	3
%define		ver	1.0.3
%define		ooo_mirror http://download.services.openoffice.org/contrib/dictionaries
Summary:	MySpell Spelling and Hyphenation dictionaries
Summary(pl.UTF-8):	Słowniki dla MySpella do sprawdzania pisowni i przenoszenia wyrazów
Name:		myspell-dictionaries
Version:	%{ver}
Release:	%{rel}
License:	BSD/GPL/LGPL
Group:		Applications/Text
URL:		http://lingucomponent.openoffice.org/download_dictionary.html
# http://openoffice.osuosl.org/contrib/dictionaries/
## Sources for spell checking dictionaries
Source100:	%{ooo_mirror}/af_ZA.zip
# Source100-md5:	6c12cd93012a04a727413d4975801604
#Source101:	%{ooo_mirror}/bg_BG.zip
Source101:	http://downloads.sourceforge.net/bgoffice/OOo-spell-bg-4.3.zip
# Source101-md5:	ee804f871c855eb218c8d825b5fe54fb
Source102:	%{ooo_mirror}/ca_ES.zip
# Source102-md5:	f0f83bd213f9cb2242173894abda37ba
Source103:	%{ooo_mirror}/cs_CZ.zip
# Source103-md5:	afe150b3aa50cc4e0eed0704e2d1cc17
Source104:	%{ooo_mirror}/cy_GB.zip
# Source104-md5:	accdb94f38555af45a54494e046a88f3
Source105:	%{ooo_mirror}/da_DK.zip
# Source105-md5:	7da0aa2b5f87ec7534df71cd6a04c6bb
Source106:	de_AT.zip
# Source106-md5:	5d079b9935f3a470960bf4bc0556179b
Source107:	de_CH.zip
# Source107-md5:	4cef76956bf62b8eda12566c6884f70d
Source108:	de_DE.zip
# Source108-md5:	886b8c3a539212ff3660a3d5eb1a8147
Source109:	%{ooo_mirror}/el_GR.zip
# Source109-md5:	02d4c0022dee569bd4733e02ef885dc4
Source110:	%{ooo_mirror}/en_AU.zip
# Source110-md5:	c39f529173d8bb0e15b1fade11dfe780
Source111:	%{ooo_mirror}/en_CA.zip
# Source111-md5:	c14942ea471a5182f376802c68933880
Source112:	en_GB.zip
# Source112-md5:	89de459a37ed6b7d9f54ad9626047e68
Source113:	en_NZ.zip
# Source113-md5:	aaf2cdd1597abdf4cfa0d9b12cfb8a29
Source114:	%{ooo_mirror}/en_US.zip
# Source114-md5:	cb1e21fee281f32d832a34ad6de1b553
Source115:	%{ooo_mirror}/es_ES.zip
# Source115-md5:	4b272f7c958dd619b2ddc007c45db53b
Source116:	%{ooo_mirror}/es_MX.zip
# Source116-md5:	e32f5ec8c94fd902a9823dae4040a019
Source117:	%{ooo_mirror}/et_EE.zip
# Source117-md5:	2a1e97d61132c537aa03df4d0fee9b89
Source118:	%{ooo_mirror}/fo_FO.zip
# Source118-md5:	c31aabce25acd791e0e41419d8d4329e
Source119:	fr_BE.zip
# Source119-md5:	6eac149eb16fc6279e93901d24b350a2
Source120:	fr_FR.zip
# Source120-md5:	5fd3aa778fe4c0ae77941c1bce18fcf7
Source121:	ga_IE.zip
# Source121-md5:	42d27da49daf068584be9592a58f3b98
Source122:	gl_ES.zip
# Source122-md5:	c9feb9d9d99baebf97d6924b81c8ecf2
Source123:	%{ooo_mirror}/he_IL.zip
# Source123-md5:	5ff2bf971a2185f65c004150ccae9965
Source124:	%{ooo_mirror}/hr_HR.zip
# Source124-md5:	0017e47e491d97c0f993a7f959b0bf01
Source125:	hu_HU.zip
# Source125-md5:	7c83480778c78cc8bef9a50d84284314
Source126:	ia_IA.zip
# Source126-md5:	b5b26537d6b8ad8ce2a84d3eb4840b62
Source127:	%{ooo_mirror}/id_ID.zip
# Source127-md5:	fe0ac356fd725cf1d5197e040fb507fc
Source128:	it_IT.zip
# Source128-md5:	4b616ce3cc57c1f9f190e3733841911e
Source129:	la_VA.zip
# Source129-md5:	299b9155bd1d3cc7555bde413d887a0e
Source130:	%{ooo_mirror}/lt_LT.zip
# Source130-md5:	3590ba02288c9092340101dca3ddc132
Source131:	%{ooo_mirror}/lv_LV.zip
# Source131-md5:	9796365409cd4387059b692679b5eff1
Source132:	%{ooo_mirror}/mi_NZ.zip
# Source132-md5:	9378de5ead3ee2759354f8ae4c7a2222
Source133:	%{ooo_mirror}/ms_MY.zip
# Source133-md5:	4b984b699541c12e1bd81b2f5f7b0050
Source134:	nb_NO.zip
# Source134-md5:	c42de27e4c12e29560f22f266f51655f
Source135:	nl_NL.zip
# Source135-md5:	24de690c4d9f9656a4d68693caa7b96c
Source136:	nn_NO.zip
# Source136-md5:	8df2f49ff333cee4cb75df444937040c
#http://www.sjp.pl/slownik/en/
Source137:	pl_PL.zip
# Source137-md5:	a1a7c9cd3f158764862329a834b44906
Source138:	%{ooo_mirror}/pt_BR.zip
# Source138-md5:	ef3a5b77535c8a35467c736fd67d73d9
Source139:	pt_PT.zip
# Source139-md5:	622f05d1e3f4d9ec6b7b691550458389
Source140:	ro_RO.zip
# Source140-md5:	d326256440b8f9744a8b803cbbb4422a
Source141:	ru_RU.zip
# Source141-md5:	a6c98684e95035cf3b49e90d4a4824b2
Source142:	sk_SK.zip
# Source142-md5:	b699bb18648e62248e4a5ae05f9b4a7b
Source143:	%{ooo_mirror}/sl_SI.zip
# Source143-md5:	74d1bf52a3c013e2a5dae2bd20ccdc00
Source144:	sv_SE.zip
# Source144-md5:	702d4dc9dc135e194086a6a270fe478d
Source145:	%{ooo_mirror}/sw_KE.zip
# Source145-md5:	af1bb4afd5e46e3624a785d1323ee6a7
Source146:	%{ooo_mirror}/uk_UA.zip
# Source146-md5:	1e067400ca6a3414d232c10ef1300293
Source147:	%{ooo_mirror}/zu_ZA.zip
# Source147-md5:	40a2ea21a81f3b08ffb46896abff66d0

## Sources for hyphenation dictionaries
Source200:	http://downloads.sourceforge.net/bgoffice/OOo-hyph-bg-4.3.zip
# Source200-md5:	34fbed48dd43d66fda133d0b05ea9c55
Source201:	%{ooo_mirror}/hyph_cs_CZ.zip
# Source201-md5:	7dc7192fb3c141db6518c54781df6846
Source202:	%{ooo_mirror}/hyph_da_DK.zip
# Source202-md5:	c398f568793bc62982f1179f2db0c119
Source203:	hyph_de.zip
# Source203-md5:	f1e532e3acc986382eb86faf7f34aa66
Source204:	%{ooo_mirror}/hyph_el_GR.zip
# Source204-md5:	73c0d55de8ad750557b0703c5004279e
Source205:	hyph_en.zip
# Source205-md5:	96fa5a6596fb41be94dde6427fc235cb
Source206:	%{ooo_mirror}/hyph_es_ES.zip
# Source206-md5:	d34ab9eefdb49147c57c01227eeb0c66
Source207:	%{ooo_mirror}/hyph_et_EE.zip
# Source207-md5:	3033df98b0975299e0b8d3b990f0e155
Source208:	%{ooo_mirror}/hyph_fi_FI.zip
# Source208-md5:	1fc88b865f919a9323d72843e860e266
Source209:	%{ooo_mirror}/hyph_fr_FR_2-0.zip
# Source209-md5:	f6d9bd51a939df943612c3f5ac2a511c
Source210:	%{ooo_mirror}/hyph_ga_IE.zip
# Source210-md5:	bd410dd925853de0dc7e5e117ac2555d
Source211:	hyph_hu.zip
# Source211-md5:	6dc2c19e6047c7faa9548cf85e93ae90
Source212:	%{ooo_mirror}/hyph_ia.zip
# Source212-md5:	63752d6c43cb6bc2eb749121ebbd9726
Source213:	%{ooo_mirror}/hyph_id_ID.zip
# Source213-md5:	f94557d7e57b22fa7e342f1c5bfe88ef
Source214:	%{ooo_mirror}/hyph_is_IS.zip
# Source214-md5:	448230e966bdf68d5f8abffd18480402
Source215:	%{ooo_mirror}/hyph_it_IT.zip
# Source215-md5:	ee57402fa3930e0641d627ec7f4f1619
Source216:	%{ooo_mirror}/hyph_lt_LT.zip
# Source216-md5:	6d90a1e831f639137077879dacb596cb
Source217:	%{ooo_mirror}/hyph_lv_LV.zip
# Source217-md5:	87e79d3a4de1f0400f513de6423ab09e
Source218:	hyph_nl.zip
# Source218-md5:	5c92b647750f310e5a432f7ffa222528
Source219:	%{ooo_mirror}/hyph_pl_PL.zip
# Source219-md5:	f4055bca56afae126cc41b49bb885e65
Source220:	%{ooo_mirror}/hyph_pt_PT.zip
# Source220-md5:	327989bbbfc9f9d56eb772427a344eb3
Source221:	%{ooo_mirror}/hyph_ru_RU.zip
# Source221-md5:	f8a8b8a368bc7394b5a4060082c44bb4
Source222:	%{ooo_mirror}/hyph_sk_SK.zip
# Source222-md5:	89ad655afadb78f6ceb87d9e1e3a675f
Source223:	%{ooo_mirror}/hyph_sl_SI.zip
# Source223-md5:	40e05217a71112257ab89ad41d4859b8
Source224:	%{ooo_mirror}/hyph_sv_SE.zip
# Source224-md5:	a1c31b48cbf570bb05f22e98dacb9e17
Source225:	%{ooo_mirror}/hyph_uk_UA.zip
# Source225-md5:	caae40c900d8e1fdd3e0ad095ce1e787

## Sources for thesaurus dictionaries
Source300:	http://downloads.sourceforge.net/bgoffice/OOo-thes-bg-4.3.zip
# Source300-md5:	11ca6156c811340f25133d70cda65ca9
Source301:	th_de_DE.zip
# Source301-md5:	2c466662e7bfe3466192ef3e6bf53d2c
Source302:	%{ooo_mirror}/thes_en_US_v2.zip
# Source302-md5:	ec611ad21ae4ee2b4415e27e252e4952
Source303:	%{ooo_mirror}/thes_es_ES_v2.zip
# Source303-md5:	e65fc3d81e98a1cda8c6725c2122a124
Source304:	th_fr_FR.zip
# Source304-md5:	4a8a55f7b1d855791e0adaa74851c90c
Source305:	th_it_IT.zip
# Source305-md5:	67735eb5aa22f084518c678a5e3a5736
#http://synonimy.ux.pl/
Source306:	th_pl_PL.zip
# Source306-md5:	dbae9faf043ab7faf58b03bd90e6b4e1
Source307:	th_sk_SK.zip
# Source307-md5:	c9842a1fb6353d5a5cf06c1757839f03
Patch0:		myspell-mozilla_words.patch
BuildRequires:	unzip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dictdir		%{_datadir}/myspell

%description
myspell-* packages contain spell checking data to be used by
OpenOffice.org or any other MySpell-capable application, like Mozilla.
myspell-hyph-* packages contain hyphenation dictionaries for a
particular set of languages.

%description -l pl.UTF-8
Pakiety myspell-* zawierają dane do sprawdzania pisowni przeznaczone
do używania przez OpenOffice.org i inne aplikacje korzystające z
MySpella, takie jak Mozilla. Pakiety myspell-hyph-* zawierają słowniki
przenoszenia wyrazów dla pewnego zbioru języków.

%package -n myspell-common
Summary:	Common files for myspell and hunspell dictionaries
Summary(pl.UTF-8):	Pliki wspólne dla słowników myspella i hunspella
License:	Public Domain
Group:		Applications/Text
Obsoletes:	mozilla-thunderbird-dictionary-ru-IE

%description -n myspell-common
Common files for myspell and hunspell dictionaries.

%description -n myspell-common -l pl.UTF-8
Pliki wspólne dla słowników myspella i hunspella.

# Spelling dictionaries
%package -n myspell-af_ZA
Summary:	MySpell spelling dictionaries for Afrikaans (South Africa)
Summary(pl.UTF-8):	Słownik dla MySpella do sprawdzania pisowni dla języka afrykanerskiego (dla Republiki Południowej Afryki)
Version:	%{ver}
# version in VERSION_af_ZA.txt
Release:	0.20060117.%{rel}
License:	LGPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}
Obsoletes:	mozilla-thunderbird-dictionary-af-ZA
Obsoletes:	myspell-af

%description -n myspell-af_ZA
myspell-af_ZA contains spell checking data in Afrikaans (South Africa)
to be used by OpenOffice.org or MySpell-capable applications like
Mozilla. With this extension, you can compose a document in Afrikaans
and check for the typos easily.

%description -n myspell-af_ZA -l pl.UTF-8
myspell-af_ZA zawiera dane do sprawdzania pisowni w języku
afrykanerskim (dla Republiki Południowej Afryki), przeznaczone do
używania przez OpenOffice.org i inne aplikacje korzystające z
MySpella, takie jak Mozilla. Przy użyciu tego rozszerzenia można łatwo
tworzyć dokumenty w języku afrykanerskim i poprawiać w nich błędy.

%package -n myspell-bg_BG
Summary:	MySpell spelling dictionaries for Bulgarian (Bulgaria)
Summary(pl.UTF-8):	Słownik dla MySpella do sprawdzania pisowni dla języka bułgarskiego (dla Bułgarii)
Version:	%{ver}
# 20100617 is mtime of release tarball from sf.net
Release:	0.20100617.%{rel}
License:	GPL/LGPL/MPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}
Obsoletes:	mozilla-thunderbird-dictionary-bg
Obsoletes:	myspell-bg
Obsoletes:	openoffice-dict-bg

%description -n myspell-bg_BG
myspell-bg_BG contains spell checking data in Bulgarian (Bulgaria) to
be used by OpenOffice.org or MySpell-capable applications like
Mozilla. With this extension, you can compose a document in Bulgarian
and check for the typos easily.

%description -n myspell-bg_BG -l pl.UTF-8
myspell-bg_BG zawiera dane do sprawdzania pisowni w języku bułgarskim
(dla Bułgarii), przeznaczone do używania przez OpenOffice.org i inne
aplikacje korzystające z MySpella, takie jak Mozilla. Przy użyciu tego
rozszerzenia można łatwo tworzyć dokumenty w języku bułgarskim i
poprawiać w nich błędy.

%package -n myspell-ca_ES
Summary:	MySpell spelling dictionaries for Catalan
Summary(pl.UTF-8):	Słownik dla MySpella do sprawdzania pisowni dla języka katalońskiego
Version:	%{ver}
Release:	0.20070724.%{rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}
Obsoletes:	mozilla-thunderbird-dictionary-ca
Obsoletes:	myspell-ca
Obsoletes:	openoffice-dict-ca

%description -n myspell-ca_ES
myspell-ca_ES contains spell checking data in Catalan to be used by
OpenOffice.org or MySpell-capable applications like Mozilla. With this
extension, you can compose a document in Catalan and check for the
typos easily.

%description -n myspell-ca_ES -l pl.UTF-8
myspell-ca_ES zawiera dane do sprawdzania pisowni w języku
katalońskim, przeznaczone do używania przez OpenOffice.org i inne
aplikacje korzystające z MySpella, takie jak Mozilla. Przy użyciu tego
rozszerzenia można łatwo tworzyć dokumenty w języku katalońskim i
poprawiać w nich błędy.

%package -n myspell-cs_CZ
Summary:	MySpell spelling dictionaries for Czech (Czech Republic)
Summary(pl.UTF-8):	Słownik dla MySpella do sprawdzania pisowni dla języka czeskiego (dla Czech)
Version:	%{ver}
Release:	0.20060303.%{rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}
Obsoletes:	mozilla-thunderbird-dictionary-cs
Obsoletes:	myspell-cs
Obsoletes:	openoffice-dict-cs

%description -n myspell-cs_CZ
myspell-cs_CZ contains spell checking data in Czech (Czech Republic)
to be used by OpenOffice.org or MySpell-capable applications like
Mozilla. With this extension, you can compose a document in Czech and
check for the typos easily.

%description -n myspell-cs_CZ -l pl.UTF-8
myspell-cs_CZ zawiera dane do sprawdzania pisowni w języku czeskim
(dla Czech), przeznaczone do używania przez OpenOffice.org i inne
aplikacje korzystające z MySpella, takie jak Mozilla. Przy użyciu tego
rozszerzenia można łatwo tworzyć dokumenty w języku czeskim i
poprawiać w nich błędy.

%package -n myspell-cy_GB
Summary:	MySpell spelling dictionaries for Welsh (Wales)
Summary(pl.UTF-8):	Słownik dla MySpella do sprawdzania pisowni dla języka walijskiego (dla Walii)
Version:	%{ver}
Release:	0.20040425.%{rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}
Obsoletes:	mozilla-thunderbird-dictionary-cy-GB
Obsoletes:	myspell-cy

%description -n myspell-cy_GB
myspell-cy_GB contains spell checking data in Welsh (Wales) to be used
by OpenOffice.org or MySpell-capable applications like Mozilla. With
this extension, you can compose a document in Welsh and check for the
typos easily.

%description -n myspell-cy_GB -l pl.UTF-8
myspell-cy_GB zawiera dane do sprawdzania pisowni w języku walijskim
(dla Walii), przeznaczone do używania przez OpenOffice.org i inne
aplikacje korzystające z MySpella, takie jak Mozilla. Przy użyciu tego
rozszerzenia można łatwo tworzyć dokumenty w języku walijskim i
poprawiać w nich błędy.

%package -n myspell-da_DK
Summary:	MySpell spelling dictionaries for Danish (Denmark)
Summary(pl.UTF-8):	Słownik dla MySpella do sprawdzania pisowni dla języka duńskiego (dla Danii)
Version:	%{ver}
# version in README_da_DK.txt
Release:	0.20070902.%{rel}
License:	LGPL v2.1+
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}
Obsoletes:	mozilla-thunderbird-dictionary-da
Obsoletes:	myspell-da
Obsoletes:	openoffice-dict-da

%description -n myspell-da_DK
myspell-da_DK contains spell checking data in Danish (Denmark) to be
used by OpenOffice.org or MySpell-capable applications like Mozilla.
With this extension, you can compose a document in Danish and check
for the typos easily.

%description -n myspell-da_DK -l pl.UTF-8
myspell-da_DK zawiera dane do sprawdzania pisowni w języku duńskim
(dla Danii), przeznaczone do używania przez OpenOffice.org i inne
aplikacje korzystające z MySpella, takie jak Mozilla. Przy użyciu tego
rozszerzenia można łatwo tworzyć dokumenty w języku duńskim i
poprawiać w nich błędy.

%package -n myspell-de_AT
Summary:	MySpell spelling dictionaries for German (Austria)
Summary(pl.UTF-8):	Słownik dla MySpella do sprawdzania pisowni dla języka niemieckiego (dla Austrii)
Version:	%{ver}
Release:	0.20100306.%{rel}
License:	GPL v2
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}
Obsoletes:	mozilla-thunderbird-dictionary-de-AT
Obsoletes:	myspell-de
Obsoletes:	openoffice-dict-de

%description -n myspell-de_AT
myspell-de_AT contains spell checking data in German (Austria) to be
used by OpenOffice.org or MySpell-capable applications like Mozilla.
With this extension, you can compose a document in German and check
for the typos easily.

%description -n myspell-de_AT -l pl.UTF-8
myspell-de_AT zawiera dane do sprawdzania pisowni w języku niemieckim
(dla Austrii), przeznaczone do używania przez OpenOffice.org i inne
aplikacje korzystające z MySpella, takie jak Mozilla. Przy użyciu tego
rozszerzenia można łatwo tworzyć dokumenty w języku niemieckim i
poprawiać w nich błędy.

%package -n myspell-de_CH
Summary:	MySpell spelling dictionaries for German (Switzerland)
Summary(pl.UTF-8):	Słownik dla MySpella do sprawdzania pisowni dla języka niemieckiego (dla Szwajcarii)
Version:	%{ver}
Release:	0.20100306.%{rel}
License:	GPL v2
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}
Obsoletes:	mozilla-thunderbird-dictionary-de-CH
Obsoletes:	myspell-de
Obsoletes:	openoffice-dict-de

%description -n myspell-de_CH
myspell-de_CH contains spell checking data in German (Switzerland) to
be used by OpenOffice.org or MySpell-capable applications like
Mozilla. With this extension, you can compose a document in German and
check for the typos easily.

%description -n myspell-de_CH -l pl.UTF-8
myspell-de_CH zawiera dane do sprawdzania pisowni w języku niemieckim
(dla Szwajcarii), przeznaczone do używania przez OpenOffice.org i inne
aplikacje korzystające z MySpella, takie jak Mozilla. Przy użyciu tego
rozszerzenia można łatwo tworzyć dokumenty w języku niemieckim i
poprawiać w nich błędy.

%package -n myspell-de_DE
Summary:	MySpell spelling dictionaries for German (Germany)
Summary(pl.UTF-8):	Słownik dla MySpella do sprawdzania pisowni dla języka niemieckiego (dla Niemiec)
Version:	%{ver}
Release:	0.20100306.%{rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}
Obsoletes:	mozilla-thunderbird-dictionary-de-DE
Obsoletes:	myspell-de
Obsoletes:	openoffice-dict-de

%description -n myspell-de_DE
myspell-de_DE contains spell checking data in German (Germany) to be
used by OpenOffice.org or MySpell-capable applications like Mozilla.
With this extension, you can compose a document in German and check
for the typos easily.

%description -n myspell-de_DE -l pl.UTF-8
myspell-de_DE zawiera dane do sprawdzania pisowni w języku niemieckim
(dla Niemiec), przeznaczone do używania przez OpenOffice.org i inne
aplikacje korzystające z MySpella, takie jak Mozilla. Przy użyciu tego
rozszerzenia można łatwo tworzyć dokumenty w języku niemieckim i
poprawiać w nich błędy.

%package -n myspell-el_GR
Summary:	MySpell spelling dictionaries for Greek (Greece)
Summary(pl.UTF-8):	Słownik dla MySpella do sprawdzania pisowni dla języka greckiego (dla Grecji)
Version:	%{ver}
# version in README_el_GR.txt
Release:	0.20041220.%{rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}
Obsoletes:	mozilla-thunderbird-dictionary-el
Obsoletes:	myspell-el
Obsoletes:	openoffice-dict-el

%description -n myspell-el_GR
myspell-el_GR contains spell checking data in Greek (Greece) to be
used by OpenOffice.org or MySpell-capable applications like Mozilla.
With this extension, you can compose a document in Greek and check for
the typos easily.

%description -n myspell-el_GR -l pl.UTF-8
myspell-el_GR zawiera dane do sprawdzania pisowni w języku greckim
(dla Grecji), przeznaczone do używania przez OpenOffice.org i inne
aplikacje korzystające z MySpella, takie jak Mozilla. Przy użyciu tego
rozszerzenia można łatwo tworzyć dokumenty w języku greckim i
poprawiać w nich błędy.

%package -n myspell-en_AU
Summary:	MySpell spelling dictionaries for English (Australian)
Summary(pl.UTF-8):	Słownik dla MySpella do sprawdzania pisowni dla języka angielskiego (dla Australii)
Version:	%{ver}
Release:	0.20030323.%{rel}
License:	LGPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}
Obsoletes:	mozilla-thunderbird-dictionary-en-AU
Obsoletes:	myspell-en
Obsoletes:	openoffice-dict-en

%description -n myspell-en_AU
myspell-en_AU contains spell checking data in English (Australian) to
be used by OpenOffice.org or MySpell-capable applications like
Mozilla. With this extension, you can compose a document in English
and check for the typos easily.

%description -n myspell-en_AU -l pl.UTF-8
myspell-en_AU zawiera dane do sprawdzania pisowni w języku angielskim
(dla Australii), przeznaczone do używania przez OpenOffice.org i inne
aplikacje korzystające z MySpella, takie jak Mozilla. Przy użyciu tego
rozszerzenia można łatwo tworzyć dokumenty w języku angielskim i
poprawiać w nich błędy.

%package -n myspell-en_CA
Summary:	MySpell spelling dictionaries for English (Canada)
Summary(pl.UTF-8):	Słownik dla MySpella do sprawdzania pisowni dla języka angielskiego (dla Kanady)
Version:	%{ver}
Release:	0.20020315.%{rel}
License:	Public Domain
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}
Obsoletes:	mozilla-thunderbird-dictionary-en-CA
Obsoletes:	myspell-en
Obsoletes:	openoffice-dict-en

%description -n myspell-en_CA
myspell-en_CA contains spell checking data in English (Canada) to be
used by OpenOffice.org or MySpell-capable applications like Mozilla.
With this extension, you can compose a document in English and check
for the typos easily.

%description -n myspell-en_CA -l pl.UTF-8
myspell-en_CA zawiera dane do sprawdzania pisowni w języku angielskim
(dla Kanady), przeznaczone do używania przez OpenOffice.org i inne
aplikacje korzystające z MySpella, takie jak Mozilla. Przy użyciu tego
rozszerzenia można łatwo tworzyć dokumenty w języku angielskim i
poprawiać w nich błędy.

%package -n myspell-en_GB
Summary:	MySpell spelling dictionaries for English (United Kingdom)
Summary(pl.UTF-8):	Słownik dla MySpella do sprawdzania pisowni dla języka angielskiego (dla Wielkiej Brytanii)
Version:	%{ver}
Release:	0.20050526.%{rel}
License:	LGPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}
Obsoletes:	mozilla-thunderbird-dictionary-en-GB
Obsoletes:	myspell-en
Obsoletes:	openoffice-dict-en

%description -n myspell-en_GB
myspell-en_GB contains spell checking data in English (United Kingdom)
to be used by OpenOffice.org or MySpell-capable applications like
Mozilla. With this extension, you can compose a document in English
and check for the typos easily.

%description -n myspell-en_GB -l pl.UTF-8
myspell-en_GB zawiera dane do sprawdzania pisowni w języku angielskim
(dla Wielkiej Brytanii), przeznaczone do używania przez OpenOffice.org
i inne aplikacje korzystające z MySpella, takie jak Mozilla. Przy
użyciu tego rozszerzenia można łatwo tworzyć dokumenty w języku
angielskim i poprawiać w nich błędy.

%package -n myspell-en_NZ
Summary:	MySpell spelling dictionaries for English (New Zealand)
Summary(pl.UTF-8):	Słownik dla MySpella do sprawdzania pisowni dla języka angielskiego (dla Nowej Zelandii)
Version:	%{ver}
Release:	0.20030906.%{rel}
License:	LGPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}
Obsoletes:	mozilla-thunderbird-dictionary-en-NZ
Obsoletes:	myspell-en
Obsoletes:	openoffice-dict-en

%description -n myspell-en_NZ
myspell-en_NZ contains spell checking data in English (New Zealand) to
be used by OpenOffice.org or MySpell-capable applications like
Mozilla. With this extension, you can compose a document in English
and check for the typos easily.

%description -n myspell-en_NZ -l pl.UTF-8
myspell-en_NZ zawiera dane do sprawdzania pisowni w języku angielskim
(dla Nowej Zelandii), przeznaczone do używania przez OpenOffice.org i
inne aplikacje korzystające z MySpella, takie jak Mozilla. Przy użyciu
tego rozszerzenia można łatwo tworzyć dokumenty w języku angielskim i
poprawiać w nich błędy.

%package -n myspell-en_US
Summary:	MySpell spelling dictionaries for English (US)
Summary(pl.UTF-8):	Słownik dla MySpella do sprawdzania pisowni dla języka angielskiego (dla Stanów Zjednoczonych)
Version:	%{ver}
Release:	0.20070504.%{rel}
License:	LGPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}
Obsoletes:	mozilla-thunderbird-dictionary-en-US
Obsoletes:	myspell-en
Obsoletes:	openoffice-dict-en

%description -n myspell-en_US
myspell-en_US contains spell checking data in English (US) to be used
by OpenOffice.org or MySpell-capable applications like Mozilla. With
this extension, you can compose a document in English and check for
the typos easily.

%description -n myspell-en_US -l pl.UTF-8
myspell-en_US zawiera dane do sprawdzania pisowni w języku angielskim
(dla Stanów Zjednoczonych), przeznaczone do używania przez
OpenOffice.org i inne aplikacje korzystające z MySpella, takie jak
Mozilla. Przy użyciu tego rozszerzenia można łatwo tworzyć dokumenty w
języku angielskim i poprawiać w nich błędy.

%package -n myspell-es_ES
Summary:	MySpell spelling dictionaries for Spanish (Spain)
Summary(pl.UTF-8):	Słownik dla MySpella do sprawdzania pisowni dla języka hiszpańskiego (dla Hiszpanii)
Version:	%{ver}
Release:	0.20051029.%{rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}
Obsoletes:	mozilla-thunderbird-dictionary-es-ES
Obsoletes:	myspell-es
Obsoletes:	openoffice-dict-es

%description -n myspell-es_ES
myspell-es_ES contains spell checking data in Spanish (Spain) to be
used by OpenOffice.org or MySpell-capable applications like Mozilla.
With this extension, you can compose a document in Spanish and check
for the typos easily.

%description -n myspell-es_ES -l pl.UTF-8
myspell-es_ES zawiera dane do sprawdzania pisowni w języku hiszpańskim
(dla Hiszpanii), przeznaczone do używania przez OpenOffice.org i inne
aplikacje korzystające z MySpella, takie jak Mozilla. Przy użyciu tego
rozszerzenia można łatwo tworzyć dokumenty w języku hiszpańskim i
poprawiać w nich błędy.

%package -n myspell-es_MX
Summary:	MySpell spelling dictionaries for Spanish (Mexico)
Summary(pl.UTF-8):	Słownik dla MySpella do sprawdzania pisowni dla języka hiszpańskiego (dla Meksyku)
Version:	%{ver}
Release:	0.20051029.%{rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}
Obsoletes:	mozilla-thunderbird-dictionary-es-MX
Obsoletes:	myspell-es
Obsoletes:	openoffice-dict-es

%description -n myspell-es_MX
myspell-es_MX contains spell checking data in Spanish (Mexico) to be
used by OpenOffice.org or MySpell-capable applications like Mozilla.
With this extension, you can compose a document in Spanish and check
for the typos easily.

%description -n myspell-es_MX -l pl.UTF-8
myspell-es_MX zawiera dane do sprawdzania pisowni w języku hiszpańskim
(dla Meksyku), przeznaczone do używania przez OpenOffice.org i inne
aplikacje korzystające z MySpella, takie jak Mozilla. Przy użyciu tego
rozszerzenia można łatwo tworzyć dokumenty w języku hiszpańskim i
poprawiać w nich błędy.

%package -n myspell-et_EE
Summary:	MySpell spelling dictionaries for Estonian (Estonia)
Summary(pl.UTF-8):	Słownik dla MySpella do sprawdzania pisowni dla języka estońskiego (dla Estonii)
Version:	%{ver}
Release:	0.20040621.%{rel}
License:	free, see http://www.eki.ee/eki/licence.html
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}
Obsoletes:	myspell-et

%description -n myspell-et_EE
myspell-et_EE contains spell checking data in Estonian (Estonia) to be
used by OpenOffice.org or MySpell-capable applications like Mozilla.
With this extension, you can compose a document in Estonian and check
for the typos easily.

%description -n myspell-et_EE -l pl.UTF-8
myspell-et_EE zawiera dane do sprawdzania pisowni w języku estońskim
(dla Estonii), przeznaczone do używania przez OpenOffice.org i inne
aplikacje korzystające z MySpella, takie jak Mozilla. Przy użyciu tego
rozszerzenia można łatwo tworzyć dokumenty w języku estońskim i
poprawiać w nich błędy.

%package -n myspell-fo_FO
Summary:	MySpell spelling dictionaries for Faroese (Faroe Islands)
Summary(pl.UTF-8):	Słownik dla MySpella do sprawdzania pisowni dla języka farerskiego (dla Wysp Owczych)
Version:	%{ver}
Release:	0.20070126.%{rel}
License:	GPL v2
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}
Obsoletes:	mozilla-thunderbird-dictionary-fo
Obsoletes:	myspell-fo

%description -n myspell-fo_FO
myspell-fo_FO contains spell checking data in Faroese (Faroe Islands)
to be used by OpenOffice.org or MySpell-capable applications like
Mozilla. With this extension, you can compose a document in Faroese
and check for the typos easily.

%description -n myspell-fo_FO -l pl.UTF-8
myspell-fo_FO zawiera dane do sprawdzania pisowni w języku farerskim
(dla Wysp Owczych), przeznaczone do używania przez OpenOffice.org i
inne aplikacje korzystające z MySpella, takie jak Mozilla. Przy użyciu
tego rozszerzenia można łatwo tworzyć dokumenty w języku fareskim i
poprawiać w nich błędy.

%package -n myspell-fr_BE
Summary:	MySpell spelling dictionaries for French (Belgium)
Summary(pl.UTF-8):	Słownik dla MySpella do sprawdzania pisowni dla języka francuskiego (dla Belgii)
Version:	%{ver}
Release:	0.20030701.%{rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}
Obsoletes:	myspell-fr
Obsoletes:	openoffice-dict-fr

%description -n myspell-fr_BE
myspell-fr_BE contains spell checking data in French (Belgium) to be
used by OpenOffice.org or MySpell-capable applications like Mozilla.
With this extension, you can compose a document in French and check
for the typos easily.

%description -n myspell-fr_BE -l pl.UTF-8
myspell-fr_BE zawiera dane do sprawdzania pisowni w języku francuskim
(dla Belgii), przeznaczone do używania przez OpenOffice.org i inne
aplikacje korzystające z MySpella, takie jak Mozilla. Przy użyciu tego
rozszerzenia można łatwo tworzyć dokumenty w języku francuskim i
poprawiać w nich błędy.

%package -n myspell-fr_FR
Summary:	MySpell spelling dictionaries for French (France)
Summary(pl.UTF-8):	Słownik dla MySpella do sprawdzania pisowni dla języka francuskiego (dla Francji)
Version:	%{ver}
Release:	0.20090914.%{rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}
Obsoletes:	myspell-fr
Obsoletes:	openoffice-dict-fr

%description -n myspell-fr_FR
myspell-fr_FR contains spell checking data in French (France) to be
used by OpenOffice.org or MySpell-capable applications like Mozilla.
With this extension, you can compose a document in French and check
for the typos easily.

%description -n myspell-fr_FR -l pl.UTF-8
myspell-fr_FR zawiera dane do sprawdzania pisowni w języku francuskim
(dla Francji), przeznaczone do używania przez OpenOffice.org i inne
aplikacje korzystające z MySpella, takie jak Mozilla. Przy użyciu tego
rozszerzenia można łatwo tworzyć dokumenty w języku francuskim i
poprawiać w nich błędy.

%package -n myspell-ga_IE
Summary:	MySpell spelling dictionaries for Irish (Ireland)
Summary(pl.UTF-8):	Słownik dla MySpella do sprawdzania pisowni dla języka irlandzkiego (dla Irlandii)
Version:	%{ver}
Release:	0.20071030.%{rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}
Obsoletes:	mozilla-thunderbird-dictionary-ga
Obsoletes:	myspell-ga
Obsoletes:	openoffice-dict-ga

%description -n myspell-ga_IE
myspell-ga_IE contains spell checking data in Irish (Ireland) to be
used by OpenOffice.org or MySpell-capable applications like Mozilla.
With this extension, you can compose a document in Irish and check for
the typos easily.

%description -n myspell-ga_IE -l pl.UTF-8
myspell-ga_IE zawiera dane do sprawdzania pisowni w języku irlandzkim
(dla Irlandii), przeznaczone do używania przez OpenOffice.org i inne
aplikacje korzystające z MySpella, takie jak Mozilla. Przy użyciu tego
rozszerzenia można łatwo tworzyć dokumenty w języku irlandzkim i
poprawiać w nich błędy.

%package -n myspell-gl_ES
Summary:	MySpell spelling dictionaries for Galician (Spain)
Summary(pl.UTF-8):	Słownik dla MySpella do sprawdzania pisowni dla języka galicyjskiego (dla Hiszpanii)
Version:	%{ver}
Release:	0.20080515.%{rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}
Obsoletes:	mozilla-thunderbird-dictionary-gl
Obsoletes:	myspell-gl
Obsoletes:	openoffice-dict-gl

%description -n myspell-gl_ES
myspell-gl_ES contains spell checking data in Galician (Spain) to be
used by OpenOffice.org or MySpell-capable applications like Mozilla.
With this extension, you can compose a document in Galician and check
for the typos easily.

%description -n myspell-gl_ES -l pl.UTF-8
myspell-gl_ES zawiera dane do sprawdzania pisowni w języku galicyjskim
(dla Hiszpanii), przeznaczone do używania przez OpenOffice.org i inne
aplikacje korzystające z MySpella, takie jak Mozilla. Przy użyciu tego
rozszerzenia można łatwo tworzyć dokumenty w języku galicyjskim i
poprawiać w nich błędy.

%package -n myspell-he_IL
Summary:	MySpell spelling dictionaries for Hebrew (Israel)
Summary(pl.UTF-8):	Słownik dla MySpella do sprawdzania pisowni dla języka hebrajskiego (dla Izraela)
Version:	%{ver}
Release:	0.20060517.%{rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}
Obsoletes:	mozilla-thunderbird-dictionary-he-IL

%description -n myspell-he_IL
myspell-he_IL contains spell checking data in Hebrew (Israel) to be
used by OpenOffice.org or MySpell-capable applications like Mozilla.
With this extension, you can compose a document in Hebrew and check
for the typos easily.

%description -n myspell-he_IL -l pl.UTF-8
myspell-he_IL zawiera dane do sprawdzania pisowni w języku hebrajskim
(dla Izraela), przeznaczone do używania przez OpenOffice.org i inne
aplikacje korzystające z MySpella, takie jak Mozilla. Przy użyciu tego
rozszerzenia można łatwo tworzyć dokumenty w języku hebrajskim i
poprawiać w nich błędy.

%package -n myspell-hr_HR
Summary:	MySpell spelling dictionaries for Croatian (Croatia)
Summary(pl.UTF-8):	Słownik dla MySpella do sprawdzania pisowni dla języka chorwackiego (dla Chorwacji)
Version:	%{ver}
Release:	0.20030928.%{rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}
Obsoletes:	mozilla-thunderbird-dictionary-hr
Obsoletes:	myspell-hr
Obsoletes:	openoffice-dict-hr

%description -n myspell-hr_HR
myspell-hr_HR contains spell checking data in Croatian (Croatia) to be
used by OpenOffice.org or MySpell-capable applications like Mozilla.
With this extension, you can compose a document in Croatian and check
for the typos easily.

%description -n myspell-hr_HR -l pl.UTF-8
myspell-hr_HR zawiera dane do sprawdzania pisowni w języku chorwackim
(dla Chorwacji), przeznaczone do używania przez OpenOffice.org i inne
aplikacje korzystające z MySpella, takie jak Mozilla. Przy użyciu tego
rozszerzenia można łatwo tworzyć dokumenty w języku chorwackim i
poprawiać w nich błędy.

%package -n myspell-hu_HU
Summary:	MySpell spelling dictionaries for Hungarian (Hungary)
Summary(pl.UTF-8):	Słownik dla MySpella do sprawdzania pisowni dla języka węgierskiego (dla Węgier)
Version:	%{ver}
Release:	0.20100206.%{rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}
Obsoletes:	mozilla-thunderbird-dictionary-hu
Obsoletes:	myspell-hu
Obsoletes:	openoffice-dict-hu

%description -n myspell-hu_HU
myspell-hu_HU contains spell checking data in Hungarian (Hungary) to
be used by OpenOffice.org or MySpell-capable applications like
Mozilla. With this extension, you can compose a document in Hungarian
and check for the typos easily.

%description -n myspell-hu_HU -l pl.UTF-8
myspell-hu_HU zawiera dane do sprawdzania pisowni w języku węgierskim
(dla Węgier), przeznaczone do używania przez OpenOffice.org i inne
aplikacje korzystające z MySpella, takie jak Mozilla. Przy użyciu tego
rozszerzenia można łatwo tworzyć dokumenty w języku węgierskim i
poprawiać w nich błędy.

%package -n myspell-ia_IA
Summary:	MySpell spelling dictionaries for Interlingua
Summary(pl.UTF-8):	Słownik dla MySpella do sprawdzania pisowni dla pomocniczego języka międzynarodowego
Version:	%{ver}
Release:	0.20050101.%{rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}
Obsoletes:	mozilla-thunderbird-dictionary-ia

%description -n myspell-ia_IA
myspell-hu_HU contains spell checking data in Interlingua to be used
by OpenOffice.org or MySpell-capable applications like Mozilla. With
this extension, you can compose a document in Interlingua and check
for the typos easily.

%description -n myspell-ia_IA -l pl.UTF-8
myspell-hu_HU zawiera dane do sprawdzania pisowni w pomocniczym języku
międzynarodowym, przeznaczone do używania przez OpenOffice.org i inne
aplikacje korzystające z MySpella, takie jak Mozilla. Przy użyciu tego
rozszerzenia można łatwo tworzyć dokumenty w pomocniczym języku
międzynarodowym i poprawiać w nich błędy.

%package -n myspell-id_ID
Summary:	MySpell spelling dictionaries for Indonesian (Indonesia)
Summary(pl.UTF-8):	Słownik dla MySpella do sprawdzania pisowni dla języka indonezyjskiego (dla Indonezji)
Version:	%{ver}
# version in README_id_ID.txt
Release:	0.20040810.%{rel}
License:	GPL v2
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}
Obsoletes:	myspell-id

%description -n myspell-id_ID
myspell-id_ID contains spell checking data in Indonesian (Indonesia)
to be used by OpenOffice.org or MySpell-capable applications like
Mozilla. With this extension, you can compose a document in Indonesian
and check for the typos easily.

%description -n myspell-id_ID -l pl.UTF-8
myspell-id_ID zawiera dane do sprawdzania pisowni w języku
indonezyjskim (dla Indonezji), przeznaczone do używania przez
OpenOffice.org i inne aplikacje korzystające z MySpella, takie jak
Mozilla. Przy użyciu tego rozszerzenia można łatwo tworzyć dokumenty w
języku indonezyjskim i poprawiać w nich błędy.

%package -n myspell-it_IT
Summary:	MySpell spelling dictionaries for Italian (Italy)
Summary(pl.UTF-8):	Słownik dla MySpella do sprawdzania pisowni dla języka włoskiego (dla Włoch)
Version:	%{ver}
Release:	0.20070901.%{rel}
License:	LGPL/GPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}
Obsoletes:	mozilla-thunderbird-dictionary-it
Obsoletes:	myspell-it
Obsoletes:	openoffice-dict-it

%description -n myspell-it_IT
myspell-it_IT contains spell checking data in Italian (Italy) to be
used by OpenOffice.org or MySpell-capable applications like Mozilla.
With this extension, you can compose a document in Italian and check
for the typos easily.

%description -n myspell-it_IT -l pl.UTF-8
myspell-it_IT zawiera dane do sprawdzania pisowni w języku włoskim
(dla Włoch), przeznaczone do używania przez OpenOffice.org i inne
aplikacje korzystające z MySpella, takie jak Mozilla. Przy użyciu tego
rozszerzenia można łatwo tworzyć dokumenty w języku włoskim i
poprawiać w nich błędy.

%package -n myspell-la_VA
Summary:	MySpell spelling dictionaries for Latin (Vatican)
Summary(pl.UTF-8):	Słownik dla MySpella do sprawdzania pisowni dla języka łacińskiego (dla Watykanu)
Version:	%{ver}
Release:	0.20060303.%{rel}
License:	LGPL/GPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}
Obsoletes:	mozilla-thunderbird-dictionary-la
Obsoletes:	openoffice-dict-la

%description -n myspell-la_VA
myspell-it_IT contains spell checking data in Latin (Vatican) to be
used by OpenOffice.org or MySpell-capable applications like Mozilla.
With this extension, you can compose a document in Latin and check for
the typos easily.

%description -n myspell-la_VA -l pl.UTF-8
myspell-it_IT zawiera dane do sprawdzania pisowni w języku łacińskim
(dla Watykanu), przeznaczone do używania przez OpenOffice.org i inne
aplikacje korzystające z MySpella, takie jak Mozilla. Przy użyciu tego
rozszerzenia można łatwo tworzyć dokumenty w języku łacińskim i
poprawiać w nich błędy.

%package -n myspell-lt_LT
Summary:	MySpell spelling dictionaries for Lithuanian (Lithuania)
Summary(pl.UTF-8):	Słownik dla MySpella do sprawdzania pisowni dla języka litewskiego (dla Litwy)
Version:	%{ver}
Release:	0.20031231.%{rel}
License:	BSD-like
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}
Obsoletes:	mozilla-thunderbird-dictionary-lt
Obsoletes:	myspell-lt
Obsoletes:	openoffice-dict-lt

%description -n myspell-lt_LT
myspell-lt_LT contains spell checking data in Lithuanian (Lithuania)
to be used by OpenOffice.org or MySpell-capable applications like
Mozilla. With this extension, you can compose a document in Lithuanian
and check for the typos easily.

%description -n myspell-lt_LT -l pl.UTF-8
myspell-lt_LT zawiera dane do sprawdzania pisowni w języku litewskim
(dla Litwy), przeznaczone do używania przez OpenOffice.org i inne
aplikacje korzystające z MySpella, takie jak Mozilla. Przy użyciu tego
rozszerzenia można łatwo tworzyć dokumenty w języku litewskim i
poprawiać w nich błędy.

%package -n myspell-lv_LV
Summary:	MySpell spelling dictionaries for Latvian (Latvia)
Summary(pl.UTF-8):	Słownik dla MySpella do sprawdzania pisowni dla języka łotewskiego (dla Łotwy)
Version:	%{ver}
# README_lv_LV.txt version 0.7.2
Release:	0.20080222.%{rel}
License:	LGPL v2.1
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}
Obsoletes:	mozilla-thunderbird-dictionary-lv_LV

%description -n myspell-lv_LV
myspell-lt_LT contains spell checking data in Latvian (Latvia) to be
used by OpenOffice.org or MySpell-capable applications like Mozilla.
With this extension, you can compose a document in Latvian and check
for the typos easily.

%description -n myspell-lv_LV -l pl.UTF-8
myspell-lt_LT zawiera dane do sprawdzania pisowni w języku łotewskim
(dla Łotwy), przeznaczone do używania przez OpenOffice.org i inne
aplikacje korzystające z MySpella, takie jak Mozilla. Przy użyciu tego
rozszerzenia można łatwo tworzyć dokumenty w języku łotewskim i
poprawiać w nich błędy.

%package -n myspell-mi_NZ
Summary:	MySpell spelling dictionaries for Maori (New Zealand)
Summary(pl.UTF-8):	Słownik dla MySpella do sprawdzania pisowni dla języka maoryjskiego (dla Nowej Zelandii)
Version:	%{ver}
# version in mi_NZ.aff
Release:	0.20080630.%{rel}
License:	LGPL
Group:		Applications/Text
URL:		http://papakupu.maori.nz/
Requires:	myspell-common = %{ver}-%{rel}
Obsoletes:	mozilla-thunderbird-dictionary-mi
Obsoletes:	myspell-mi

%description -n myspell-mi_NZ
myspell-mi_NZ contains spell checking data in Maori (New Zealand) to
be used by OpenOffice.org or MySpell-capable applications like
Mozilla. With this extension, you can compose a document in Maori and
check for the typos easily.

%description -n myspell-mi_NZ -l pl.UTF-8
myspell-mi_NZ zawiera dane do sprawdzania pisowni w języku maoryjskim
(dla Nowej Zelandii), przeznaczone do używania przez OpenOffice.org i
inne aplikacje korzystające z MySpella, takie jak Mozilla. Przy użyciu
tego rozszerzenia można łatwo tworzyć dokumenty w języku maoryjskim i
poprawiać w nich błędy.

%package -n myspell-ms_MY
Summary:	MySpell spelling dictionaries for Malay (Malaysia)
Summary(pl.UTF-8):	Słownik dla MySpella do sprawdzania pisowni dla języka malajskiego (dla Malezji)
Version:	%{ver}
# version 20041230 in README_ms_MY.txt, but mtime 20050117
Release:	0.20050117.%{rel}
License:	GNU Free Documentation License
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}
Obsoletes:	mozilla-thunderbird-dictionary-ms
Obsoletes:	myspell-ms

%description -n myspell-ms_MY
myspell-ms_MY contains spell checking data in Malay (Malaysia) to be
used by OpenOffice.org or MySpell-capable applications like Mozilla.
With this extension, you can compose a document in Malay and check for
the typos easily.

%description -n myspell-ms_MY -l pl.UTF-8
myspell-ms_MY zawiera dane do sprawdzania pisowni w języku malajskim
(dla Malezji), przeznaczone do używania przez OpenOffice.org i inne
aplikacje korzystające z MySpella, takie jak Mozilla. Przy użyciu tego
rozszerzenia można łatwo tworzyć dokumenty w języku malajskim i
poprawiać w nich błędy.

%package -n myspell-nb_NO
Summary:	MySpell spelling dictionaries for Norwegian/Bokmaal (Norway)
Summary(pl.UTF-8):	Słownik dla MySpella do sprawdzania pisowni dla języka norweskiego bokmaal (dla Norwegii)
Version:	%{ver}
Release:	0.20080310.%{rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}
Obsoletes:	mozilla-thunderbird-dictionary-nb
Obsoletes:	myspell-no
Obsoletes:	openoffice-dict-nb

%description -n myspell-nb_NO
myspell-nb_NO contains spell checking data in Norwegian Bokmaal
(Norway) to be used by OpenOffice.org or MySpell-capable applications
like Mozilla. With this extension, you can compose a document in
Norwegian Bokmaal and check for the typos easily.

%description -n myspell-nb_NO -l pl.UTF-8
myspell-nb_NO zawiera dane do sprawdzania pisowni w języku norweskim
bokmaal (dla Norwegii), przeznaczone do używania przez OpenOffice.org
i inne aplikacje korzystające z MySpella, takie jak Mozilla. Przy
użyciu tego rozszerzenia można łatwo tworzyć dokumenty w języku
norweskim bokmaal i poprawiać w nich błędy.

%package -n myspell-nl_NL
Summary:	MySpell spelling dictionaries for Dutch (Netherland)
Summary(pl.UTF-8):	Słownik dla MySpella do sprawdzania pisowni dla języka holenderskiego (dla Holandii)
Version:	%{ver}
Release:	0.20090722.%{rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}
Obsoletes:	mozilla-thunderbird-dictionary-nl
Obsoletes:	myspell-nl
Obsoletes:	openoffice-dict-nl

%description -n myspell-nl_NL
myspell-nl_NL contains spell checking data in Dutch (Netherland) to be
used by OpenOffice.org or MySpell-capable applications like Mozilla.
With this extension, you can compose a document in Dutch and check for
the typos easily.

%description -n myspell-nl_NL -l pl.UTF-8
myspell-nl_NL zawiera dane do sprawdzania pisowni w języku
holenderskim (dla Holandii), przeznaczone do używania przez
OpenOffice.org i inne aplikacje korzystające z MySpella, takie jak
Mozilla. Przy użyciu tego rozszerzenia można łatwo tworzyć dokumenty w
języku holenderskim i poprawiać w nich błędy.

%package -n myspell-nn_NO
Summary:	MySpell spelling dictionaries for Norwegian/Nynorsk (Norway)
Summary(pl.UTF-8):	Słownik dla MySpella do sprawdzania pisowni dla języka norweskiego nynorsk (dla Norwegii)
Version:	%{ver}
Release:	0.20080310.%{rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}
Obsoletes:	mozilla-thunderbird-dictionary-nn
Obsoletes:	myspell-no
Obsoletes:	openoffice-dict-nn

%description -n myspell-nn_NO
myspell-nn_NO contains spell checking data in Norwegian/Nynorsk
(Norway) to be used by OpenOffice.org or MySpell-capable applications
like Mozilla. With this extension, you can compose a document in
Norwegian/Nynorsk and check for the typos easily.

%description -n myspell-nn_NO -l pl.UTF-8
myspell-nn_NO zawiera dane do sprawdzania pisowni w języku norweskim
nynorsk (dla Norwegii), przeznaczone do używania przez OpenOffice.org
i inne aplikacje korzystające z MySpella, takie jak Mozilla. Przy
użyciu tego rozszerzenia można łatwo tworzyć dokumenty w języku
norweskim nynorsk i poprawiać w nich błędy.

%package -n myspell-pl_PL
Summary:	MySpell spelling dictionaries for Polish (Poland)
Summary(pl.UTF-8):	Słownik dla MySpella do sprawdzania pisowni dla języka polskiego (dla Polski)
Version:	%{ver}
Release:	0.20100310.%{rel}
License:	Creative Commons ShareAlike, http://creativecommons.org/licenses/sa/1.0
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}
Obsoletes:	mozilla-thunderbird-dictionary-pl
Obsoletes:	myspell-pl
Obsoletes:	openoffice-dict-pl
Obsoletes:	openoffice-dict-pl-alt

%description -n myspell-pl_PL
myspell-pl_PL contains spell checking data in Polish (Poland) to be
used by OpenOffice.org or MySpell-capable applications like Mozilla.
With this extension, you can compose a document in Polish and check
for the typos easily.

%description -n myspell-pl_PL -l pl.UTF-8
myspell-pl_PL zawiera dane do sprawdzania pisowni w języku polskim
(dla Polski), przeznaczone do używania przez OpenOffice.org i inne
aplikacje korzystające z MySpella, takie jak Mozilla. Przy użyciu tego
rozszerzenia można łatwo tworzyć dokumenty w języku polskim i
poprawiać w nich błędy.

%package -n myspell-pt_BR
Summary:	MySpell spelling dictionaries for Portuguese (Brasil)
Summary(pl.UTF-8):	Słownik dla MySpella do sprawdzania pisowni dla języka portugalskiego (dla Brazylii)
Version:	%{ver}
Release:	0.20070606.%{rel}
License:	LGPL v2.1
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}
Obsoletes:	mozilla-thunderbird-dictionary-pt-BR
Obsoletes:	openoffice-dict-pt

%description -n myspell-pt_BR
myspell-pt_BR contains spell checking data in Portuguese (Brasil) to
be used by OpenOffice.org or MySpell-capable applications like
Mozilla. With this extension, you can compose a document in Portuguese
and check for the typos easily.

%description -n myspell-pt_BR -l pl.UTF-8
myspell-pt_BR zawiera dane do sprawdzania pisowni w języku
portugalskim (dla Brazylii), przeznaczone do używania przez
OpenOffice.org i inne aplikacje korzystające z MySpella, takie jak
Mozilla. Przy użyciu tego rozszerzenia można łatwo tworzyć dokumenty w
języku portugalskim i poprawiać w nich błędy.

%package -n myspell-pt_PT
Summary:	MySpell spelling dictionaries for Portuguese (Portugal)
Summary(pl.UTF-8):	Słownik dla MySpella do sprawdzania pisowni dla języka portugalskiego (dla Portugalii)
Version:	%{ver}
Release:	0.20091013.%{rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}
Obsoletes:	mozilla-thunderbird-dictionary-pt
Obsoletes:	myspell-pt
Obsoletes:	openoffice-dict-pt

%description -n myspell-pt_PT
myspell-pt_PT contains spell checking data in Portuguese (Portugal) to
be used by OpenOffice.org or MySpell-capable applications like
Mozilla. With this extension, you can compose a document in Portuguese
and check for the typos easily.

%description -n myspell-pt_PT -l pl.UTF-8
myspell-pt_PT zawiera dane do sprawdzania pisowni w języku
portugalskim (dla Portugalii), przeznaczone do używania przez
OpenOffice.org i inne aplikacje korzystające z MySpella, takie jak
Mozilla. Przy użyciu tego rozszerzenia można łatwo tworzyć dokumenty w
języku portugalskim i poprawiać w nich błędy.

%package -n myspell-ro_RO
Summary:	MySpell spelling dictionaries for Romanian (Romania)
Summary(pl.UTF-8):	Słownik dla MySpella do sprawdzania pisowni dla języka rumuńskiego (dla Rumunii)
Version:	%{ver}
Release:	0.20091108.%{rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}
Obsoletes:	mozilla-thunderbird-dictionary-ro
Obsoletes:	myspell-ro

%description -n myspell-ro_RO
myspell-ro_RO contains spell checking data in Romanian (Romania) to be
used by OpenOffice.org or MySpell-capable applications like Mozilla.
With this extension, you can compose a document in Romanian and check
for the typos easily.

%description -n myspell-ro_RO -l pl.UTF-8
myspell-ro_RO zawiera dane do sprawdzania pisowni w języku rumuńskim
(dla Rumunii), przeznaczone do używania przez OpenOffice.org i inne
aplikacje korzystające z MySpella, takie jak Mozilla. Przy użyciu tego
rozszerzenia można łatwo tworzyć dokumenty w języku rumuńskim i
poprawiać w nich błędy.

%package -n myspell-ru_RU
Summary:	MySpell spelling dictionaries for Russian (Russia)
Summary(pl.UTF-8):	Słownik dla MySpella do sprawdzania pisowni dla języka rosyjskiego (dla Rosji)
Version:	%{ver}
Release:	0.20090603.%{rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}
Obsoletes:	mozilla-thunderbird-dictionary-ru
Obsoletes:	myspell-ru
Obsoletes:	openoffice-dict-ru

%description -n myspell-ru_RU
myspell-ru_RU contains spell checking data in Russian (Russia) to be
used by OpenOffice.org or MySpell-capable applications like Mozilla.
With this extension, you can compose a document in Russian and check
for the typos easily.

%description -n myspell-ru_RU -l pl.UTF-8
myspell-ru_RU zawiera dane do sprawdzania pisowni w języku rosyjskim
(dla Rosji), przeznaczone do używania przez OpenOffice.org i inne
aplikacje korzystające z MySpella, takie jak Mozilla. Przy użyciu tego
rozszerzenia można łatwo tworzyć dokumenty w języku rosyjskim i
poprawiać w nich błędy.

%package -n myspell-sk_SK
Summary:	MySpell spelling dictionaries for Slovak (Slovak Republic)
Summary(pl.UTF-8):	Słownik dla MySpella do sprawdzania pisowni dla języka słowackiego (dla Słowacji)
Version:	%{ver}
Release:	0.20100208.%{rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}
Obsoletes:	mozilla-thunderbird-dictionary-sk
Obsoletes:	myspell-sk
Obsoletes:	openoffice-dict-sk

%description -n myspell-sk_SK
myspell-sk_SK contains spell checking data in Slovak (Slovak Republic)
to be used by OpenOffice.org or MySpell-capable applications like
Mozilla. With this extension, you can compose a document in Slovak and
check for the typos easily.

%description -n myspell-sk_SK -l pl.UTF-8
myspell-sk_SK zawiera dane do sprawdzania pisowni w języku słowackim
(dla Słowacji), przeznaczone do używania przez OpenOffice.org i inne
aplikacje korzystające z MySpella, takie jak Mozilla. Przy użyciu tego
rozszerzenia można łatwo tworzyć dokumenty w języku słowackim i
poprawiać w nich błędy.

%package -n myspell-sl_SI
Summary:	MySpell spelling dictionaries for Slovenian (Slovenia)
Summary(pl.UTF-8):	Słownik dla MySpella do sprawdzania pisowni dla języka słoweńskiego (dla Słowenii)
Version:	%{ver}
Release:	0.20030907.%{rel}
License:	GPL, LGPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}
Obsoletes:	mozilla-thunderbird-dictionary-sl
Obsoletes:	myspell-sl
Obsoletes:	openoffice-dict-sl

%description -n myspell-sl_SI
myspell-sl_SI contains spell checking data in Slovenian (Slovenia) to
be used by OpenOffice.org or MySpell-capable applications like
Mozilla. With this extension, you can compose a document in Slovenian
and check for the typos easily.

%description -n myspell-sl_SI -l pl.UTF-8
myspell-sl_SI zawiera dane do sprawdzania pisowni w języku słoweńskim
(dla Słowenii), przeznaczone do używania przez OpenOffice.org i inne
aplikacje korzystające z MySpella, takie jak Mozilla. Przy użyciu tego
rozszerzenia można łatwo tworzyć dokumenty w języku słoweńskim i
poprawiać w nich błędy.

%package -n myspell-sv_SE
Summary:	MySpell spelling dictionaries for Swedish (Sweden)
Summary(pl.UTF-8):	Słownik dla MySpella do sprawdzania pisowni dla języka szwedzkiego (dla Szwecji)
Version:	%{ver}
Release:	0.20100131.%{rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}
Obsoletes:	mozilla-thunderbird-dictionary-sv
Obsoletes:	myspell-sv
Obsoletes:	openoffice-dict-sv

%description -n myspell-sv_SE
myspell-sv_SE contains spell checking data in Swedish (Sweden) to be
used by OpenOffice.org or MySpell-capable applications like Mozilla.
With this extension, you can compose a document in Swedish and check
for the typos easily.

%description -n myspell-sv_SE -l pl.UTF-8
myspell-sv_SE zawiera dane do sprawdzania pisowni w języku szwedzkim
(dla Szwecji), przeznaczone do używania przez OpenOffice.org i inne
aplikacje korzystające z MySpella, takie jak Mozilla. Przy użyciu tego
rozszerzenia można łatwo tworzyć dokumenty w języku szwedzkim i
poprawiać w nich błędy.

%package -n myspell-sw_KE
Summary:	MySpell spelling dictionaries for Kiswahili (Africa)
Summary(pl.UTF-8):	Słownik dla MySpella do sprawdzania pisowni dla języka suahili (dla Afryki)
Version:	%{ver}
# version 20040316 in README_sw_KE.txt, files mtime 20040515
Release:	0.20040515.%{rel}
License:	LGPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}
Obsoletes:	myspell-sw

%description -n myspell-sw_KE
myspell-sw_KE contains spell checking data in Kiswahili (Africa) to be
used by OpenOffice.org or MySpell-capable applications like Mozilla.
With this extension, you can compose a document in Kiswahili and check
for the typos easily.

%description -n myspell-sw_KE -l pl.UTF-8
myspell-sw_KE zawiera dane do sprawdzania pisowni w języku suahili
(dla Afryki), przeznaczone do używania przez OpenOffice.org i inne
aplikacje korzystające z MySpella, takie jak Mozilla. Przy użyciu tego
rozszerzenia można łatwo tworzyć dokumenty w języku suahili i
poprawiać w nich błędy.

%package -n myspell-uk_UA
Summary:	MySpell spelling dictionaries for Ukrainian (Ukraine)
Summary(pl.UTF-8):	Słownik dla MySpella do sprawdzania pisowni dla języka ukraińskiego (dla Ukrainy)
Version:	%{ver}
# version in README_uk_UA.txt is 1.5.7, files mtime 20090124
Release:	0.20090124.%{rel}
License:	GPL, LGPL and MPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}
Obsoletes:	mozilla-thunderbird-dictionary-uk
Obsoletes:	myspell-uk
Obsoletes:	openoffice-dict-uk

%description -n myspell-uk_UA
myspell-uk_UA contains spell checking data in Ukrainian (Ukraine) to
be used by OpenOffice.org or MySpell-capable applications like
Mozilla. With this extension, you can compose a document in Ukrainian
and check for the typos easily.

%description -n myspell-uk_UA -l pl.UTF-8
myspell-uk_UA zawiera dane do sprawdzania pisowni w języku ukraińskim
(dla Ukrainy), przeznaczone do używania przez OpenOffice.org i inne
aplikacje korzystające z MySpella, takie jak Mozilla. Przy użyciu tego
rozszerzenia można łatwo tworzyć dokumenty w języku ukraińskim i
poprawiać w nich błędy.

%package -n myspell-zu_ZA
Summary:	MySpell spelling dictionaries for Zulu (South Africa)
Summary(pl.UTF-8):	Słownik dla MySpella do sprawdzania pisowni dla języka zuluskiego (dla Republiki Południowej Afryki)
Version:	%{ver}
# version 20060120 in VERSION_zu_ZA.txt, files mtime 20060124
Release:	0.20060124.%{rel}
License:	LGPL v2.1
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}
Obsoletes:	mozilla-thunderbird-dictionary-zu-ZA
Obsoletes:	myspell-zu

%description -n myspell-zu_ZA
myspell-zu_ZA contains spell checking data in Zulu (South Africa) to
be used by OpenOffice.org or MySpell-capable applications like
Mozilla. With this extension, you can compose a document in Zulu and
check for the typos easily.

%description -n myspell-zu_ZA -l pl.UTF-8
myspell-zu_ZA zawiera dane do sprawdzania pisowni w języku zuluskim
(dla Republiki Południowej Afryki), przeznaczone do używania przez
OpenOffice.org i inne aplikacje korzystające z MySpella, takie jak
Mozilla. Przy użyciu tego rozszerzenia można łatwo tworzyć dokumenty w
języku zuluskim i poprawiać w nich błędy.

# Hyphenation
%package -n myspell-hyph-bg
Summary:	MySpell hyphenation dictionaries for Bulgarian
Summary(pl.UTF-8):	Słowniki przenoszenia wyrazów dla MySpella dla języka bułgarskiego
Version:	%{ver}
# 20100617 is mtime of release tarball from sf.net
Release:	0.20100617.%{rel}
License:	GPL/LGPL/MPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}

%description -n myspell-hyph-bg
myspell-hyph-bg contains hyphenation data for Bulgarian to be used by
OpenOffice.org or MySpell-capable applications like Mozilla.

%description -n myspell-hyph-bg -l pl.UTF-8
myspell-hyph-bg zawiera dane do przenoszenia wyrazów dla języka
bułgarskiego, przeznaczone do używania przez OpenOffice.org i inne
aplikacje korzystające z Myspella, takie jak Mozilla.

%package -n myspell-hyph-cs
Summary:	MySpell hyphenation dictionaries for Czech
Summary(pl.UTF-8):	Słowniki przenoszenia wyrazów dla MySpella dla języka czeskiego
Version:	%{ver}
Release:	0.20031228.%{rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}

%description -n myspell-hyph-cs
myspell-hyph-cs contains hyphenation data for Czech to be used by
OpenOffice.org or MySpell-capable applications like Mozilla.

%description -n myspell-hyph-cs -l pl.UTF-8
myspell-hyph-cs zawiera dane do przenoszenia wyrazów dla języka
czeskiego, przeznaczone do używania przez OpenOffice.org i inne
aplikacje korzystające z Myspella, takie jak Mozilla.

%package -n myspell-hyph-da
Summary:	MySpell hyphenation dictionaries for Danish
Summary(pl.UTF-8):	Słowniki przenoszenia wyrazów dla MySpella dla języka duńskiego
Version:	%{ver}
Release:	0.20030904.%{rel}
License:	LGPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}

%description -n myspell-hyph-da
myspell-hyph-da contains hyphenation data for Danish to be used by
OpenOffice.org or MySpell-capable applications like Mozilla.

%description -n myspell-hyph-da -l pl.UTF-8
myspell-hyph-da zawiera dane do przenoszenia wyrazów dla języka
duńskiego, przeznaczone do używania przez OpenOffice.org i inne
aplikacje korzystające z Myspella, takie jak Mozilla.

%package -n myspell-hyph-de
Summary:	MySpell hyphenation dictionaries for German
Summary(pl.UTF-8):	Słowniki przenoszenia wyrazów dla MySpella dla języka niemieckiego
Version:	%{ver}
Release:	0.20100113.%{rel}
License:	LGPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}

%description -n myspell-hyph-de
myspell-hyph-de contains hyphenation data for German to be used by
OpenOffice.org or MySpell-capable applications like Mozilla.

%description -n myspell-hyph-de -l pl.UTF-8
myspell-hyph-de zawiera dane do przenoszenia wyrazów dla języka
niemieckiego, przeznaczone do używania przez OpenOffice.org i inne
aplikacje korzystające z Myspella, takie jak Mozilla.

%package -n myspell-hyph-el
Summary:	MySpell hyphenation dictionaries for Greek
Summary(pl.UTF-8):	Słowniki przenoszenia wyrazów dla MySpella dla języka greckiego
Version:	%{ver}
Release:	0.20051017.%{rel}
License:	LGPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}

%description -n myspell-hyph-el
myspell-hyph-el contains hyphenation data for Greek to be used by
OpenOffice.org or MySpell-capable applications like Mozilla.

%description -n myspell-hyph-el -l pl.UTF-8
myspell-hyph-el zawiera dane do przenoszenia wyrazów dla języka
greckiego, przeznaczone do używania przez OpenOffice.org i inne
aplikacje korzystające z Myspella, takie jak Mozilla.

%package -n myspell-hyph-en
Summary:	MySpell hyphenation dictionaries for English
Summary(pl.UTF-8):	Słowniki przenoszenia wyrazów dla MySpella dla języka angielskiego
Version:	%{ver}
Release:	0.20020608.%{rel}
License:	LGPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}

%description -n myspell-hyph-en
myspell-hyph-en contains hyphenation data for English to be used by
OpenOffice.org or MySpell-capable applications like Mozilla.

%description -n myspell-hyph-en -l pl.UTF-8
myspell-hyph-en zawiera dane do przenoszenia wyrazów dla języka
angielskiego, przeznaczone do używania przez OpenOffice.org i inne
aplikacje korzystające z Myspella, takie jak Mozilla.

%package -n myspell-hyph-es
Summary:	MySpell hyphenation dictionaries for Spanish
Summary(pl.UTF-8):	Słowniki przenoszenia wyrazów dla MySpella dla języka hiszpańskiego
Version:	%{ver}
Release:	0.20050201.%{rel}
License:	LGPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}

%description -n myspell-hyph-es
myspell-hyph-es contains hyphenation data for Spanish to be used by
OpenOffice.org or MySpell-capable applications like Mozilla.

%description -n myspell-hyph-es -l pl.UTF-8
myspell-hyph-es zawiera dane do przenoszenia wyrazów dla języka
hiszpańskiego, przeznaczone do używania przez OpenOffice.org i inne
aplikacje korzystające z Myspella, takie jak Mozilla.

%package -n myspell-hyph-et
Summary:	MySpell hyphenation dictionaries for Estonian
Summary(pl.UTF-8):	Słowniki przenoszenia wyrazów dla MySpella dla języka estońskiego
Version:	%{ver}
Release:	0.20040718.%{rel}
License:	free, see http://www.eki.ee/eki/licence.html
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}

%description -n myspell-hyph-et
myspell-hyph-et contains hyphenation data for Estonian to be used by
OpenOffice.org or MySpell-capable applications like Mozilla.

%description -n myspell-hyph-et -l pl.UTF-8
myspell-hyph-et zawiera dane do przenoszenia wyrazów dla języka
estońskiego, przeznaczone do używania przez OpenOffice.org i inne
aplikacje korzystające z Myspella, takie jak Mozilla.

%package -n myspell-hyph-fi
Summary:	MySpell hyphenation dictionaries for Finnish
Summary(pl.UTF-8):	Słowniki przenoszenia wyrazów dla MySpella dla języka fińskiego
Version:	%{ver}
Release:	0.20040816.%{rel}
License:	freely distributable
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}

%description -n myspell-hyph-fi
myspell-hyph-fi contains hyphenation data for Finnish to be used by
OpenOffice.org or MySpell-capable applications like Mozilla.

%description -n myspell-hyph-fi -l pl.UTF-8
myspell-hyph-fi zawiera dane do przenoszenia wyrazów dla języka
fińskiego, przeznaczone do używania przez OpenOffice.org i inne
aplikacje korzystające z Myspella, takie jak Mozilla.

%package -n myspell-hyph-fr
Summary:	MySpell hyphenation dictionaries for French
Summary(pl.UTF-8):	Słowniki przenoszenia wyrazów dla MySpella dla języka francuskiego
Version:	%{ver}
Release:	0.20080318.%{rel}
License:	LGPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}

%description -n myspell-hyph-fr
myspell-hyph-fr contains hyphenation data for French to be used by
OpenOffice.org or MySpell-capable applications like Mozilla.

%description -n myspell-hyph-fr -l pl.UTF-8
myspell-hyph-fr zawiera dane do przenoszenia wyrazów dla języka
francuskiego, przeznaczone do używania przez OpenOffice.org i inne
aplikacje korzystające z Myspella, takie jak Mozilla.

%package -n myspell-hyph-ga
Summary:	MySpell hyphenation dictionaries for Irish
Summary(pl.UTF-8):	Słowniki przenoszenia wyrazów dla MySpella dla języka irlandzkiego
Version:	%{ver}
Release:	0.20040816.%{rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}

%description -n myspell-hyph-ga
myspell-hyph-ga contains hyphenation data for Irish to be used by
OpenOffice.org or MySpell-capable applications like Mozilla.

%description -n myspell-hyph-ga -l pl.UTF-8
myspell-hyph-ga zawiera dane do przenoszenia wyrazów dla języka
irlandzkiego, przeznaczone do używania przez OpenOffice.org i inne
aplikacje korzystające z Myspella, takie jak Mozilla.

%package -n myspell-hyph-hu
Summary:	MySpell hyphenation dictionaries for Hungarian
Summary(pl.UTF-8):	Słowniki przenoszenia wyrazów dla MySpella dla języka węgierskiego
Version:	%{ver}
Release:	0.20100212.%{rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}

%description -n myspell-hyph-hu
myspell-hyph-hu contains hyphenation data for Hungarian to be used by
OpenOffice.org or MySpell-capable applications like Mozilla.

%description -n myspell-hyph-hu -l pl.UTF-8
myspell-hyph-hu zawiera dane do przenoszenia wyrazów dla języka
węgierskiego, przeznaczone do używania przez OpenOffice.org i inne
aplikacje korzystające z Myspella, takie jak Mozilla.

%package -n myspell-hyph-ia
Summary:	MySpell hyphenation dictionaries for Interlingua
Summary(pl.UTF-8):	Słowniki przenoszenia wyrazów dla MySpella dla pomocniczego języka międzynarodowego
Version:	%{ver}
Release:	0.20050228.%{rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}

%description -n myspell-hyph-ia
myspell-hyph-ia contains hyphenation data for Interlingua to be used
by OpenOffice.org or MySpell-capable applications like Mozilla.

%description -n myspell-hyph-ia -l pl.UTF-8
myspell-hyph-ia zawiera dane do przenoszenia wyrazów dla pomocniczego
języka międzynarodowego, przeznaczone do używania przez OpenOffice.org
i inne aplikacje korzystające z Myspella, takie jak Mozilla.

%package -n myspell-hyph-id
Summary:	MySpell hyphenation dictionaries for Indonesian
Summary(pl.UTF-8):	Słowniki przenoszenia wyrazów dla MySpella dla języka indonezyjskiego
Version:	%{ver}
Release:	0.20040816.%{rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}

%description -n myspell-hyph-id
myspell-hyph-id contains hyphenation data for Indonesian to be used by
OpenOffice.org or MySpell-capable applications like Mozilla.

%description -n myspell-hyph-id -l pl.UTF-8
myspell-hyph-id zawiera dane do przenoszenia wyrazów dla języka
indonezyjskiego, przeznaczone do używania przez OpenOffice.org i inne
aplikacje korzystające z Myspella, takie jak Mozilla.

%package -n myspell-hyph-is
Summary:	MySpell hyphenation dictionaries for Icelandic
Summary(pl.UTF-8):	Słowniki przenoszenia wyrazów dla MySpella dla języka islandzkiego
Version:	%{ver}
Release:	0.20040816.%{rel}
License:	LGPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}

%description -n myspell-hyph-is
myspell-hyph-is contains hyphenation data for Icelandic to be used by
OpenOffice.org or MySpell-capable applications like Mozilla.

%description -n myspell-hyph-is -l pl.UTF-8
myspell-hyph-is zawiera dane do przenoszenia wyrazów dla języka
islandzkiego, przeznaczone do używania przez OpenOffice.org i inne
aplikacje korzystające z Myspella, takie jak Mozilla.

%package -n myspell-hyph-it
Summary:	MySpell hyphenation dictionaries for Italian
Summary(pl.UTF-8):	Słowniki przenoszenia wyrazów dla MySpella dla języka włoskiego
Version:	%{ver}
Release:	0.20071126.%{rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}

%description -n myspell-hyph-it
myspell-hyph-it contains hyphenation data for Italian to be used by
OpenOffice.org or MySpell-capable applications like Mozilla.

%description -n myspell-hyph-it -l pl.UTF-8
myspell-hyph-it zawiera dane do przenoszenia wyrazów dla języka
włoskiego, przeznaczone do używania przez OpenOffice.org i inne
aplikacje korzystające z Myspella, takie jak Mozilla.

%package -n myspell-hyph-lt
Summary:	MySpell hyphenation dictionaries for Lithuanian
Summary(pl.UTF-8):	Słowniki przenoszenia wyrazów dla MySpella dla języka litewskiego
Version:	%{ver}
Release:	0.20040816.%{rel}
License:	LPPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}

%description -n myspell-hyph-lt
myspell-hyph-lt contains hyphenation data for Lithuanian to be used by
OpenOffice.org or MySpell-capable applications like Mozilla.

%description -n myspell-hyph-lt -l pl.UTF-8
myspell-hyph-lt zawiera dane do przenoszenia wyrazów dla języka
litewskiego, przeznaczone do używania przez OpenOffice.org i inne
aplikacje korzystające z Myspella, takie jak Mozilla.

%package -n myspell-hyph-lv
Summary:	MySpell hyphenation dictionaries for Latvian
Summary(pl.UTF-8):	Słowniki przenoszenia wyrazów dla MySpella dla języka łotewskiego
Version:	%{ver}
Release:	0.20050914.%{rel}
License:	LPPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}

%description -n myspell-hyph-lv
myspell-hyph-lv contains hyphenation data for Latvian to be used by
OpenOffice.org or MySpell-capable applications like Mozilla.

%description -n myspell-hyph-lv -l pl.UTF-8
myspell-hyph-lv zawiera dane do przenoszenia wyrazów dla języka
łotewskiego, przeznaczone do używania przez OpenOffice.org i inne
aplikacje korzystające z Myspella, takie jak Mozilla.

%package -n myspell-hyph-nl
Summary:	MySpell hyphenation dictionaries for Dutch
Summary(pl.UTF-8):	Słowniki przenoszenia wyrazów dla MySpella dla języka holenderskiego
Version:	%{ver}
Release:	0.20080829.%{rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}

%description -n myspell-hyph-nl
myspell-hyph-nl contains hyphenation data for Dutch to be used by
OpenOffice.org or MySpell-capable applications like Mozilla.

%description -n myspell-hyph-nl -l pl.UTF-8
myspell-hyph-nl zawiera dane do przenoszenia wyrazów dla języka
holenderskiego, przeznaczone do używania przez OpenOffice.org i inne
aplikacje korzystające z Myspella, takie jak Mozilla.

%package -n myspell-hyph-pl
Summary:	MySpell hyphenation dictionaries for Polish
Summary(pl.UTF-8):	Słowniki przenoszenia wyrazów dla MySpella dla języka polskiego
Version:	%{ver}
Release:	0.20070407.%{rel}
License:	LGPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}

%description -n myspell-hyph-pl
myspell-hyph-pl contains hyphenation data for Polish to be used by
OpenOffice.org or MySpell-capable applications like Mozilla.

%description -n myspell-hyph-pl -l pl.UTF-8
myspell-hyph-pl zawiera dane do przenoszenia wyrazów dla języka
polskiego, przeznaczone do używania przez OpenOffice.org i inne
aplikacje korzystające z Myspella, takie jak Mozilla.

%package -n myspell-hyph-pt
Summary:	MySpell hyphenation dictionaries for Portuguese
Summary(pl.UTF-8):	Słowniki przenoszenia wyrazów dla MySpella dla języka portugalskiego
Version:	%{ver}
Release:	0.20040816.%{rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}

%description -n myspell-hyph-pt
myspell-hyph-pt contains hyphenation data for Portuguese to be used by
OpenOffice.org or MySpell-capable applications like Mozilla.

%description -n myspell-hyph-pt -l pl.UTF-8
myspell-hyph-pt zawiera dane do przenoszenia wyrazów dla języka
portugalskiego, przeznaczone do używania przez OpenOffice.org i inne
aplikacje korzystające z Myspella, takie jak Mozilla.

%package -n myspell-hyph-ru
Summary:	MySpell hyphenation dictionaries for Russian
Summary(pl.UTF-8):	Słowniki przenoszenia wyrazów dla MySpella dla języka rosyjskiego
Version:	%{ver}
Release:	0.20030908.%{rel}
License:	LGPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}

%description -n myspell-hyph-ru
myspell-hyph-ru contains hyphenation data for Russian to be used by
OpenOffice.org or MySpell-capable applications like Mozilla.

%description -n myspell-hyph-ru -l pl.UTF-8
myspell-hyph-ru zawiera dane do przenoszenia wyrazów dla języka
rosyjskiego, przeznaczone do używania przez OpenOffice.org i inne
aplikacje korzystające z Myspella, takie jak Mozilla.

%package -n myspell-hyph-sk
Summary:	MySpell hyphenation dictionaries for Slovak
Summary(pl.UTF-8):	Słowniki przenoszenia wyrazów dla MySpella dla języka słowackiego
Version:	%{ver}
Release:	0.20060323.%{rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}

%description -n myspell-hyph-sk
myspell-hyph-sk contains hyphenation data for Slovak to be used by
OpenOffice.org or MySpell-capable applications like Mozilla.

%description -n myspell-hyph-sk -l pl.UTF-8
myspell-hyph-sk zawiera dane do przenoszenia wyrazów dla języka
słowackiego, przeznaczone do używania przez OpenOffice.org i inne
aplikacje korzystające z Myspella, takie jak Mozilla.

%package -n myspell-hyph-sl
Summary:	MySpell hyphenation dictionaries for Slovenian
Summary(pl.UTF-8):	Słowniki przenoszenia wyrazów dla MySpella dla języka słoweńskiego
Version:	%{ver}
Release:	0.20030904.%{rel}
License:	Copyright Matjaz Vrecko
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}

%description -n myspell-hyph-sl
myspell-hyph-sl contains hyphenation data for Slovenian to be used by
OpenOffice.org or MySpell-capable applications like Mozilla.

%description -n myspell-hyph-sl -l pl.UTF-8
myspell-hyph-sl zawiera dane do przenoszenia wyrazów dla języka
słoweńskiego, przeznaczone do używania przez OpenOffice.org i inne
aplikacje korzystające z Myspella, takie jak Mozilla.

%package -n myspell-hyph-sv
Summary:	MySpell hyphenation dictionaries for Swedish
Summary(pl.UTF-8):	Słowniki przenoszenia wyrazów dla MySpella dla języka szwedzkiego
Version:	%{ver}
Release:	0.20030814.%{rel}
License:	LGPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}

%description -n myspell-hyph-sv
myspell-hyph-sv contains hyphenation data for Swedish to be used by
OpenOffice.org or MySpell-capable applications like Mozilla.

%description -n myspell-hyph-sv -l pl.UTF-8
myspell-hyph-sv zawiera dane do przenoszenia wyrazów dla języka
szwedzkiego, przeznaczone do używania przez OpenOffice.org i inne
aplikacje korzystające z Myspella, takie jak Mozilla.

%package -n myspell-hyph-uk
Summary:	MySpell hyphenation dictionaries for Ukrainian
Summary(pl.UTF-8):	Słowniki przenoszenia wyrazów dla MySpella dla języka ukraińskiego
Version:	%{ver}
Release:	0.20030904.%{rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}

%description -n myspell-hyph-uk
myspell-hyph-uk contains hyphenation data for Ukrainian to be used by
OpenOffice.org or MySpell-capable applications like Mozilla.

%description -n myspell-hyph-uk -l pl.UTF-8
myspell-hyph-uk zawiera dane do przenoszenia wyrazów dla języka
ukraińskiego, przeznaczone do używania przez OpenOffice.org i inne
aplikacje korzystające z Myspella, takie jak Mozilla.

# Thesaurus
%package -n myspell-thes-bg_BG
Summary:	MySpell thesaurus for Bulgarian (Bulgaria)
Summary(pl.UTF-8):	Słownik wyrazów bliskoznacznych dla MySpella dla języka bułgarskiego (dla Bułgarii)
Version:	%{ver}
# 20100617 is mtime of release tarball from sf.net
Release:	0.20100617.%{rel}
License:	GPL/LGPL/MPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}

%description -n myspell-thes-bg_BG
myspell-thes-bg_BG contains thesaurus data in Bulgarian (Bulgaria) to
be used by MySpell-capable applications like OpenOffice.org.

%description -n myspell-thes-bg_BG -l pl.UTF-8
myspell-thes-bg_BG zawiera dane wyrazów bliskoznacznych w języku
bułgarskim (dla Bułgarii), przeznaczone do używania przez aplikacje
korzystające z MySpella, takie jak OpenOffice.org.

%package -n myspell-thes-de_DE
Summary:	MySpell thesaurus for German (Germany)
Summary(pl.UTF-8):	Słownik wyrazów bliskoznacznych dla MySpella dla języka niemieckiego (dla Niemiec)
Version:	%{ver}
Release:	0.20100307.%{rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}
Obsoletes:	openoffice-thesaurus-de

%description -n myspell-thes-de_DE
myspell-thes-de_DE contains thesaurus data in German (Germany) to be
used by MySpell-capable applications like OpenOffice.org.

%description -n myspell-thes-de_DE -l pl.UTF-8
myspell-thes-de_DE zawiera dane wyrazów bliskoznacznych w języku
niemieckim (dla Niemiec), przeznaczone do używania przez aplikacje
korzystające z MySpella, takie jak OpenOffice.org.

%package -n myspell-thes-en_US
Summary:	MySpell thesaurus for English (US)
Summary(pl.UTF-8):	Słownik wyrazów bliskoznacznych dla MySpella dla języka angielskiego (dla Stanów Zjednoczonych)
Version:	%{ver}
Release:	0.20051125.%{rel}
License:	BSD
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}
Obsoletes:	openoffice-thesaurus-en

%description -n myspell-thes-en_US
myspell-thes-en_US contains thesaurus data in English (US) to be used
by MySpell-capable applications like OpenOffice.org.

%description -n myspell-thes-en_US -l pl.UTF-8
myspell-thes-en_US zawiera dane wyrazów bliskoznacznych w języku
angielskim (dla Stanów Zjednoczonych), przeznaczone do używania przez
aplikacje korzystające z MySpella, takie jak OpenOffice.org.

%package -n myspell-thes-es_ES
Summary:	MySpell thesaurus for Spanish (Spain)
Summary(pl.UTF-8):	Słownik wyrazów bliskoznacznych dla MySpella dla języka hiszpańskiego (dla Hiszpanii)
Version:	%{ver}
Release:	0.20050720.%{rel}
License:	LGPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}
Obsoletes:	openoffice-thesaurus-es

%description -n myspell-thes-es_ES
myspell-thes-es_ES contains thesaurus data in Spanish (Spain) to be
used by MySpell-capable applications like OpenOffice.org.

%description -n myspell-thes-es_ES -l pl.UTF-8
myspell-thes-es_ES zawiera dane wyrazów bliskoznacznych w języku
hiszpańskim (dla Hiszpanii), przeznaczone do używania przez aplikacje
korzystające z MySpella, takie jak OpenOffice.org.

%package -n myspell-thes-fr_FR
Summary:	MySpell thesaurus for French (France)
Summary(pl.UTF-8):	Słownik wyrazów bliskoznacznych dla MySpella dla języka francuskiego (dla Francji)
Version:	%{ver}
Release:	0.20090911.%{rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}

%description -n myspell-thes-fr_FR
myspell-thes-fr_FR contains thesaurus data in French (France) to be
used by MySpell-capable applications like OpenOffice.org.

%description -n myspell-thes-fr_FR -l pl.UTF-8
myspell-thes-fr_FR zawiera dane wyrazów bliskoznacznych w języku
francuskim (dla Francji), przeznaczone do używania przez aplikacje
korzystające z MySpella, takie jak OpenOffice.org.

%package -n myspell-thes-it_IT
Summary:	MySpell thesaurus for Italian (Italy)
Summary(pl.UTF-8):	Słownik wyrazów bliskoznacznych dla MySpella dla języka włoskiego (dla Włoch)
Version:	%{ver}
Release:	0.20081129.%{rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}

%description -n myspell-thes-it_IT
myspell-thes-it_IT contains thesaurus data in Italian (Italy) to be
used by MySpell-capable applications like OpenOffice.org.

%description -n myspell-thes-it_IT -l pl.UTF-8
myspell-thes-it_IT zawiera dane wyrazów bliskoznacznych w języku
włoskim (dla Włoch), przeznaczone do używania przez aplikacje
korzystające z MySpella, takie jak OpenOffice.org.

%package -n myspell-thes-pl_PL
Summary:	MySpell thesaurus for Polish (Poland)
Summary(pl.UTF-8):	Słownik wyrazów bliskoznacznych dla MySpella dla języka polskiego (dla Polski)
Version:	%{ver}
Release:	0.20080513.%{rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}
Obsoletes:	openoffice-thesaurus-pl-alt
Obsoletes:	openoffice.org-thesaurus-pl-alt

%description -n myspell-thes-pl_PL
myspell-thes-pl_PL contains thesaurus data in Polish (Poland) to be
used by MySpell-capable applications like OpenOffice.org.

%description -n myspell-thes-pl_PL -l pl.UTF-8
myspell-thes-pl_PL zawiera dane wyrazów bliskoznacznych w języku
polskim (dla Polski), przeznaczone do używania przez aplikacje
korzystające z MySpella, takie jak OpenOffice.org.

%package -n myspell-thes-sk_SK
Summary:	MySpell thesaurus for Slovak (Slovak Republic)
Summary(pl.UTF-8):	Słownik wyrazów bliskoznacznych dla MySpella dla języka słowackiego (dla Słowacji)
Version:	%{ver}
Release:	0.20100207.%{rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{ver}-%{rel}

%description -n myspell-thes-sk_SK
myspell-thes-sk_SK contains thesaurus data in Slovak (Slovak Republic)
to be used by MySpell-capable applications like OpenOffice.org.

%description -n myspell-thes-sk_SK -l pl.UTF-8
myspell-thes-sk_SK zawiera dane wyrazów bliskoznacznych w języku
słowackim (dla Słowacji), przeznaczone do używania przez aplikacje
korzystające z MySpella, takie jak OpenOffice.org.

%prep
%setup -qcT

# Handle spelling dictionaries
for dictfile in %{SOURCE100} %{SOURCE101} %{SOURCE102} %{SOURCE103} %{SOURCE104} \
		%{SOURCE105} %{SOURCE106} %{SOURCE107} %{SOURCE108} %{SOURCE109} \
		%{SOURCE110} %{SOURCE111} %{SOURCE112} %{SOURCE113} %{SOURCE114} \
		%{SOURCE115} %{SOURCE116} %{SOURCE117} %{SOURCE118} %{SOURCE119} \
		%{SOURCE120} %{SOURCE121} %{SOURCE122} %{SOURCE123} %{SOURCE124} \
		%{SOURCE125} %{SOURCE126} %{SOURCE127} %{SOURCE128} %{SOURCE129} \
		%{SOURCE130} %{SOURCE131} %{SOURCE132} %{SOURCE133} %{SOURCE134} \
		%{SOURCE135} %{SOURCE136} %{SOURCE137} %{SOURCE138} %{SOURCE139} \
		%{SOURCE140} %{SOURCE141} %{SOURCE142} %{SOURCE143} %{SOURCE144} \
		%{SOURCE145} %{SOURCE146} %{SOURCE147}; do
	basefile="${dictfile##*/}"
	langpack="${basefile%.zip}"
	langfile=$langpack
	# name fixups
	case "$langpack" in
	OOo-spell-bg*)
		langfile=$langpack/bg_BG
		langpack=bg_BG
	;;
	esac
	echo "LANGPACK=$langpack"
	install -d doc/DICT/$langpack
	%{__unzip} -q -d doc/DICT/$langpack $dictfile
	install -d dic/DICT/$langpack
	mv doc/DICT/$langpack/$langfile.aff dic/DICT/$langpack/$langpack.aff
	mv doc/DICT/$langpack/$langfile.dic dic/DICT/$langpack/$langpack.dic
	# create dummy file if docdir is empty
	if ! ls doc/DICT/$langpack/*; then
		cat > doc/DICT/$langpack/README_$langpack.txt << EOF
Spell checking dictionary for $langpack
EOF
	fi
done

# Handle spelling dictionaries
for hyphfile in %{SOURCE200} %{SOURCE201} %{SOURCE202} %{SOURCE203} %{SOURCE204} \
		%{SOURCE205} %{SOURCE206} %{SOURCE207} %{SOURCE208} %{SOURCE209} \
		%{SOURCE210} %{SOURCE211} %{SOURCE212} %{SOURCE213} %{SOURCE214} \
		%{SOURCE215} %{SOURCE216} %{SOURCE217} %{SOURCE218} %{SOURCE219} \
		%{SOURCE220} %{SOURCE221} %{SOURCE222} %{SOURCE223} %{SOURCE224} \
		%{SOURCE225}; do
	basefile=${hyphfile##*/}
	langpack=${basefile%.zip}
	langfile=$langpack
	# name fixups
	case "$langpack" in
	OOo-hyph-bg*)
		langfile=$langpack/hyph_bg_BG
		langpack=hyph_bg_BG
	;;
	hyph_fr_FR_2-0)
		langpack=hyph_fr
		langfile=hyph_fr_FR
	;;
	hyph_es_ES)
		langpack=hyph_es
		langfile=hyph_es_ES
	;;
	hyph_en_US)
		langpack=hyph_en
		langfile=hyph_es_US
	;;
	hyph_it_IT)
		langpack=hyph_it
		langfile=hyph_it_IT
	;;
	hyph_pt_PT)
		langpack=hyph_pt
		langfile=hyph_pt_PT
	;;
	esac
	echo "LANGPACK/(HPY)=$langpack"
	install -d doc/HYPH/$langpack
	%{__unzip} -q -d doc/HYPH/$langpack $hyphfile
	install -d dic/HYPH/$langpack
	mv doc/HYPH/$langpack/$langfile.dic dic/HYPH/$langpack/$langpack.dic
	# create dummy file if docdir is empty
	if ! ls doc/HYPH/$langpack/*; then
		cat > doc/HYPH/$langpack/README_$langpack.txt << EOF
Hyphenation dictionary for $langpack
EOF
	fi
done

# Handle thesaurus dictionaries
for thesfile in %{SOURCE300} %{SOURCE301} %{SOURCE302} %{SOURCE303} %{SOURCE304} \
		%{SOURCE305} %{SOURCE306} %{SOURCE307}; do
	basefile=${thesfile##*/}
	langpack=${basefile%.zip}
	langfile=$langpack
	# name fixups
	case "$langpack" in
	OOo-thes-bg*)
		langfile=$langpack/th_bg_BG
		langpack=th_bg_BG
	;;
	thes_en_US_v2)
		langpack=th_en_US
		langfile=th_en_US_v2
	;;
	thes_es_ES_v2)
		langpack=th_es_ES
		langfile=th_es_ES_v2
	;;
	esac
	echo "LANGPACK(thes)=$langpack"
	install -d doc/THES/$langpack
	%{__unzip} -q -d doc/THES/$langpack $thesfile
	install -d dic/THES/$langpack
	mv doc/THES/$langpack/$langfile.dat dic/THES/$langpack/$langpack.dat
	mv doc/THES/$langpack/$langfile.idx dic/THES/$langpack/$langpack.idx
	# create dummy file if docdir is empty
	if ! ls doc/THES/$langpack/*; then
		cat > doc/THES/$langpack/README_$langpack.txt << EOF
Thesaurus dictionary for $langpack
EOF
	fi
done

# no subdirs there
mv doc/DICT/bg_BG/{OOo-spell-bg-*/*,}
rmdir doc/DICT/bg_BG/OOo-spell-bg-*
mv doc/HYPH/hyph_bg_BG/{OOo-hyph-bg-*/*,}
rmdir doc/HYPH/hyph_bg_BG/OOo-hyph-bg-*
mv doc/THES/th_bg_BG/{OOo-thes-bg-*/*,}
rmdir doc/THES/th_bg_BG/OOo-thes-bg-*

# remove common docs
find -name GPL-2.0.txt | xargs rm -v
find -name LGPL-2.1.txt | xargs rm -v
find -name MPL-1.1.txt | xargs rm -v

%patch -P0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{dictdir}

# Install spell checking dictionaries
for file in dic/DICT/*/*; do
	cp -p $file $RPM_BUILD_ROOT%{dictdir}/${file##*/}
done

# Install hyphenation dictionaries
for file in dic/HYPH/*/*; do
	cp -p $file $RPM_BUILD_ROOT%{dictdir}/${file##*/}
done

# Install thesaurus dictionaries
for file in dic/THES/*/*; do
	cp -p $file $RPM_BUILD_ROOT%{dictdir}/${file##*/}
done

touch $RPM_BUILD_ROOT%{dictdir}/dictionary.lst

%clean
rm -rf $RPM_BUILD_ROOT

##
## Scripts for spell checking

# ooo-build-ooe680-m6/build/ooe680-m6/dictionaries/diclst/dictionary.lst describes:
# List of All Dictionaries to be Loaded by OpenOffice
# ---------------------------------------------------
# Each Entry in the list have the following space delimited fields
#
# Field 1: Entry Type "DICT" - spellchecking dictionary
#                     "HYPH" - hyphenation dictionary
#                     "THES" - thesaurus files
# List of All Dictionaries to be Loaded by OpenOffice
# ---------------------------------------------------
# Each Entry in the list have the following space delimited fields
#
# Field 1: Entry Type "DICT" - spellchecking dictionary
#                     "HYPH" - hyphenation dictionary
#                     "THES" - thesaurus files
#
# Field 2: Language code from Locale "en" or "de" or "pt" ...
#
# Field 3: Country Code from Locale "US" or "GB" or "PT"
#
# Field 4: Root name of file(s) "en_US" or "hyph_de" or "th_en_US
#          (do not add extensions to the name)

%post -n myspell-af_ZA
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*af[ \t]*ZA[ \t]*af_ZA" %{dictdir}/dictionary.lst; then
	echo "DICT af ZA af_ZA" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-af_ZA
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^DICT.*af.*ZA.*af_ZA$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-bg_BG
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*bg[ \t]*BG[ \t]*bg_BG" %{dictdir}/dictionary.lst; then
	echo "DICT bg BG bg_BG" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-bg_BG
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^DICT.*bg.*BG.*bg_BG$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-ca_ES
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*ca[ \t]*ES[ \t]*ca_ES" %{dictdir}/dictionary.lst; then
	echo "DICT ca ES ca_ES" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-ca_ES
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^DICT.*ca.*ES.*ca_ES$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-cs_CZ
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*cs[ \t]*CZ[ \t]*cs_CZ" %{dictdir}/dictionary.lst; then
	echo "DICT cs CZ cs_CZ" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-cs_CZ
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^DICT.*cs.*CZ.*cs_CZ$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-cy_GB
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*cy[ \t]*GB[ \t]*cy_GB" %{dictdir}/dictionary.lst; then
	echo "DICT cy GB cy_GB" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-cy_GB
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^DICT.*cy.*GB.*cy_GB$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-da_DK
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*da[ \t]*DK[ \t]*da_DK" %{dictdir}/dictionary.lst; then
	echo "DICT da DK da_DK" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-da_DK
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^DICT.*da.*DK.*da_DK$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-de_AT
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*de[ \t]*AT[ \t]*de_AT" %{dictdir}/dictionary.lst; then
	echo "DICT de AT de_AT" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-de_AT
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^DICT.*de.*AT.*de_AT$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-el_GR
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*el[ \t]*GR[ \t]*el_GR" %{dictdir}/dictionary.lst; then
	echo "DICT el GR el_GR" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-el_GR
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^DICT.*el.*GR.*el_GR$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-en_US
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*en[ \t]*US[ \t]*en_US" %{dictdir}/dictionary.lst; then
	echo "DICT en US en_US" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-en_US
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^DICT.*en.*US.*en_US$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-en_NZ
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*en[ \t]*NZ[ \t]*en_NZ" %{dictdir}/dictionary.lst; then
	echo "DICT en NZ en_NZ" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-en_NZ
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^DICT.*en.*NZ.*en_NZ$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-es_MX
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*es[ \t]*MX[ \t]*es_MX" %{dictdir}/dictionary.lst; then
	echo "DICT es MX es_MX" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*es[ \t]*AR[ \t]*es_MX" %{dictdir}/dictionary.lst; then
	echo "DICT es AR es_MX" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*es[ \t]*CO[ \t]*es_MX" %{dictdir}/dictionary.lst; then
	echo "DICT es CO es_MX" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-es_MX
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^DICT.*es.*MX.*es_MX$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^DICT.*es.*AR.*es_MX$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^DICT.*es.*CO.*es_MX$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-et_EE
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*et[ \t]*EE[ \t]*et_EE" %{dictdir}/dictionary.lst; then
	echo "DICT et EE et_EE" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-et_EE
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^DICT.*et.*EE.*et_EE$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-fo_FO
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*fo[ \t]*FO[ \t]*fo_FO" %{dictdir}/dictionary.lst; then
	echo "DICT fo FO fo_FO" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-fo_FO
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^DICT.*fo.*FO.*fo_FO$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-fr_BE
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*fr[ \t]*BE[ \t]*fr_BE" %{dictdir}/dictionary.lst; then
	echo "DICT fr BE fr_BE" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-fr_BE
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^DICT.*fr.*BE.*fr_BE$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-ga_IE
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*ga[ \t]*IE[ \t]*ga_IE" %{dictdir}/dictionary.lst; then
	echo "DICT ga IE ga_IE" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-ga_IE
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^DICT.*ga.*IE.*ga_IE$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-gl_ES
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*gl[ \t]*ES[ \t]*gl_ES" %{dictdir}/dictionary.lst; then
	echo "DICT gl ES gl_ES" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-gl_ES
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^DICT.*gl.*ES.*gl_ES$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-he_IL
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*he[ \t]*IL[ \t]*he_IL" %{dictdir}/dictionary.lst; then
	echo "DICT he IL he_IL" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-he_IL
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^DICT.*he.*IL.*he_IL$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-hr_HR
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*hr[ \t]*HR[ \t]*hr_HR" %{dictdir}/dictionary.lst; then
	echo "DICT hr HR hr_HR" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-hr_HR
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^DICT.*hr.*HR.*hr_HR$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-hu_HU
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*hu[ \t]*HU[ \t]*hu_HU" %{dictdir}/dictionary.lst; then
	echo "DICT hu HU hu_HU" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-hu_HU
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^DICT.*hu.*HU.*hu_HU$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-ia_IA
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*ia[ \t]*IA[ \t]*ia_IA" %{dictdir}/dictionary.lst; then
	echo "DICT ia IA ia_IA" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-ia_IA
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^DICT.*ia.*IA.*ia_IA$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-id_ID
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*id[ \t]*ID[ \t]*id_ID" %{dictdir}/dictionary.lst; then
	echo "DICT id ID id_ID" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-id_ID
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^DICT.*id.*ID.*id_ID$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-it_IT
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*it[ \t]*IT[ \t]*it_IT" %{dictdir}/dictionary.lst; then
	echo "DICT it IT it_IT" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-it_IT
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^DICT.*it.*IT.*it_IT$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-la_VA
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*la[ \t]*VA[ \t]*la_VA" %{dictdir}/dictionary.lst; then
	echo "DICT la VA la_VA" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-la_VA
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^DICT.*la.*VA.*la_VA$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-lt_LT
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*lt[ \t]*LT[ \t]*lt_LT" %{dictdir}/dictionary.lst; then
	echo "DICT lt LT lt_LT" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-lt_LT
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^DICT.*lt.*LT.*lt_LT$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-mi_NZ
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*mi[ \t]*NZ[ \t]*mi_NZ" %{dictdir}/dictionary.lst; then
	echo "DICT mi NZ mi_NZ" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-mi_NZ
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^DICT.*mi.*NZ.*mi_NZ$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-ms_MY
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*ms[ \t]*MY[ \t]*ms_MY" %{dictdir}/dictionary.lst; then
	echo "DICT ms MY ms_MY" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-ms_MY
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^DICT.*ms.*MY.*ms_MY$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-nb_NO
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*nb[ \t]*NO[ \t]*nb_NO" %{dictdir}/dictionary.lst; then
	echo "DICT nb NO nb_NO" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-nb_NO
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^DICT.*nb.*NO.*nb_NO$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-nl_NL
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*nl[ \t]*NL[ \t]*nl_NL" %{dictdir}/dictionary.lst; then
	echo "DICT nl NL nl_NL" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-nl_NL
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^DICT.*nl.*NL.*nl_NL$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-nn_NO
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*nn[ \t]*NO[ \t]*nn_NO" %{dictdir}/dictionary.lst; then
	echo "DICT nn NO nn_NO" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-nn_NO
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^DICT.*nn.*NO.*nn_NO$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-pl_PL
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*pl[ \t]*PL[ \t]*pl_PL" %{dictdir}/dictionary.lst; then
	echo "DICT pl PL pl_PL" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-pl_PL
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^DICT.*pl.*PL.*pl_PL$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-pt_BR
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*pt[ \t]*BR[ \t]*pt_BR" %{dictdir}/dictionary.lst; then
	echo "DICT pt BR pt_BR" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-pt_BR
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^DICT.*pt.*BR.*pt_BR$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-ro_RO
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*ro[ \t]*RO[ \t]*ro_RO" %{dictdir}/dictionary.lst; then
	echo "DICT ro RO ro_RO" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-ro_RO
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^DICT.*ro.*RO.*ro_RO$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-ru_RU
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*ru[ \t]*RU[ \t]*ru_RU" %{dictdir}/dictionary.lst; then
	echo "DICT ru RU ru_RU" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-ru_RU
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^DICT.*ru.*RU.*ru_RU$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-sk_SK
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*sk[ \t]*SK[ \t]*sk_SK" %{dictdir}/dictionary.lst; then
	echo "DICT sk SK sk_SK" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-sk_SK
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^DICT.*sk.*SK.*sk_SK$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-sl_SI
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*sl[ \t]*SI[ \t]*sl_SI" %{dictdir}/dictionary.lst; then
	echo "DICT sl SI sl_SI" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-sl_SI
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^DICT.*sl.*SI.*sl_SI$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-sv_SE
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*sv[ \t]*SE[ \t]*sv_SE" %{dictdir}/dictionary.lst; then
	echo "DICT sv SE sv_SE" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-sv_SE
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^DICT.*sv.*SE.*sv_SE$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-sw_KE
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*sw[ \t]*KE[ \t]*sw_KE" %{dictdir}/dictionary.lst; then
	echo "DICT sw KE sw_KE" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-sw_KE
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^DICT.*sw.*KE.*sw_KE$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-uk_UA
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*uk[ \t]*UA[ \t]*uk_UA" %{dictdir}/dictionary.lst; then
	echo "DICT uk UA uk_UA" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-uk_UA
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^DICT.*uk.*UA.*uk_UA$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-zu_ZA
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*zu[ \t]*ZA[ \t]*zu_ZA" %{dictdir}/dictionary.lst; then
	echo "DICT zu ZA zu_ZA" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-zu_ZA
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^DICT.*zu.*ZA.*zu_ZA$/d' %{dictdir}/dictionary.lst
fi

##
## Scripts for hyphenation
##
%post -n myspell-hyph-bg
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*bg[ \t]*BG[ \t]*hyph_bg_BG" %{dictdir}/dictionary.lst; then
	umask 002
	echo "HYPH bg BG hyph_bg_BG" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-hyph-bg
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^HYPH.*bg.*BG.*hyph_bg_BG$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-hyph-cs
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*cs[ \t]*CZ[ \t]*hyph_cs_CZ" %{dictdir}/dictionary.lst; then
	umask 002
	echo "HYPH cs CZ hyph_cs_CZ" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-hyph-cs
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^HYPH.*cs.*CZ.*hyph_cs_CZ$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-hyph-da
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*da[ \t]*DA[ \t]*hyph_da_DK" %{dictdir}/dictionary.lst; then
	umask 002
	echo "HYPH da DK hyph_da_DK" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-hyph-da
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^HYPH.*da.*DK.*hyph_da_DK$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-hyph-de
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*de[ \t]*DE[ \t]*hyph_de" %{dictdir}/dictionary.lst; then
	echo "HYPH de DE hyph_de" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*de[ \t]*AT[ \t]*hyph_de" %{dictdir}/dictionary.lst; then
	echo "HYPH de AT hyph_de" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*de[ \t]*CH[ \t]*hyph_de" %{dictdir}/dictionary.lst; then
	echo "HYPH de CH hyph_de" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*de[ \t]*LI[ \t]*hyph_de" %{dictdir}/dictionary.lst; then
	echo "HYPH de LI hyph_de" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*de[ \t]*LU[ \t]*hyph_de" %{dictdir}/dictionary.lst; then
	echo "HYPH de LU hyph_de" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-hyph-de
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^HYPH.*de.*AT.*hyph_de$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^HYPH.*de.*CH.*hyph_de$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^HYPH.*de.*DE.*hyph_de$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^HYPH.*de.*LI.*hyph_de$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^HYPH.*de.*LU.*hyph_de$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-hyph-el
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*el[ \t]*GR[ \t]*hyph_el_GR" %{dictdir}/dictionary.lst; then
	umask 002
	echo "HYPH el GR hyph_el_GR" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-hyph-el
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^HYPH.*el.*GR.*hyph_el_GR$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-hyph-en
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*en[ \t]*US[ \t]*hyph_en" %{dictdir}/dictionary.lst; then
	echo "HYPH en US hyph_en" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*en[ \t]*CA[ \t]*hyph_en" %{dictdir}/dictionary.lst; then
	echo "HYPH en CA hyph_en" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*en[ \t]*GB[ \t]*hyph_en" %{dictdir}/dictionary.lst; then
	echo "HYPH en GB hyph_en" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*en[ \t]*NZ[ \t]*hyph_en" %{dictdir}/dictionary.lst; then
	echo "HYPH en NZ hyph_en" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*en[ \t]*AU[ \t]*hyph_en" %{dictdir}/dictionary.lst; then
	echo "HYPH en AU hyph_en" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*en[ \t]*BZ[ \t]*hyph_en" %{dictdir}/dictionary.lst; then
	echo "HYPH en BZ hyph_en" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*en[ \t]*ZA[ \t]*hyph_en" %{dictdir}/dictionary.lst; then
	echo "HYPH en ZA hyph_en" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*en[ \t]*IE[ \t]*hyph_en" %{dictdir}/dictionary.lst; then
	echo "HYPH en IE hyph_en" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*en[ \t]*JM[ \t]*hyph_en" %{dictdir}/dictionary.lst; then
	echo "HYPH en JM hyph_en" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*en[ \t]*PH[ \t]*hyph_en" %{dictdir}/dictionary.lst; then
	echo "HYPH en PH hyph_en" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*en[ \t]*TT[ \t]*hyph_en" %{dictdir}/dictionary.lst; then
	echo "HYPH en TT hyph_en" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*en[ \t]*ZW[ \t]*hyph_en" %{dictdir}/dictionary.lst; then
	echo "HYPH en ZW hyph_en" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-hyph-en
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^HYPH.*en.*AU.*hyph_en$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^HYPH.*en.*BZ.*hyph_en$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^HYPH.*en.*CA.*hyph_en$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^HYPH.*en.*GB.*hyph_en$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^HYPH.*en.*IE.*hyph_en$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^HYPH.*en.*JM.*hyph_en$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^HYPH.*en.*NZ.*hyph_en$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^HYPH.*en.*PH.*hyph_en$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^HYPH.*en.*TT.*hyph_en$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^HYPH.*en.*US.*hyph_en$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^HYPH.*en.*ZA.*hyph_en$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^HYPH.*en.*ZW.*hyph_en$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-hyph-es
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*es[ \t]*ES[ \t]*hyph_es" %{dictdir}/dictionary.lst; then
	echo "HYPH es ES hyph_es" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*es[ \t]*AR[ \t]*hyph_es" %{dictdir}/dictionary.lst; then
	echo "HYPH es AR hyph_es" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*es[ \t]*BZ[ \t]*hyph_es" %{dictdir}/dictionary.lst; then
	echo "HYPH es BZ hyph_es" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*es[ \t]*BO[ \t]*hyph_es" %{dictdir}/dictionary.lst; then
	echo "HYPH es BO hyph_es" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*es[ \t]*CL[ \t]*hyph_es" %{dictdir}/dictionary.lst; then
	echo "HYPH es CL hyph_es" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*es[ \t]*CO[ \t]*hyph_es" %{dictdir}/dictionary.lst; then
	echo "HYPH es CO hyph_es" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*es[ \t]*CR[ \t]*hyph_es" %{dictdir}/dictionary.lst; then
	echo "HYPH es CR hyph_es" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*es[ \t]*CU[ \t]*hyph_es" %{dictdir}/dictionary.lst; then
	echo "HYPH es CU hyph_es" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*es[ \t]*DO[ \t]*hyph_es" %{dictdir}/dictionary.lst; then
	echo "HYPH es DO hyph_es" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*es[ \t]*EC[ \t]*hyph_es" %{dictdir}/dictionary.lst; then
	echo "HYPH es EC hyph_es" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*es[ \t]*SV[ \t]*hyph_es" %{dictdir}/dictionary.lst; then
	echo "HYPH es SV hyph_es" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*es[ \t]*GU[ \t]*hyph_es" %{dictdir}/dictionary.lst; then
	echo "HYPH es GU hyph_es" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*es[ \t]*JN[ \t]*hyph_es" %{dictdir}/dictionary.lst; then
	echo "HYPH es JN hyph_es" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*es[ \t]*MX[ \t]*hyph_es" %{dictdir}/dictionary.lst; then
	echo "HYPH es MX hyph_es" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*es[ \t]*NI[ \t]*hyph_es" %{dictdir}/dictionary.lst; then
	echo "HYPH es NI hyph_es" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*es[ \t]*PA[ \t]*hyph_es" %{dictdir}/dictionary.lst; then
	echo "HYPH es PA hyph_es" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*es[ \t]*PU[ \t]*hyph_es" %{dictdir}/dictionary.lst; then
	echo "HYPH es PU hyph_es" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*es[ \t]*PE[ \t]*hyph_es" %{dictdir}/dictionary.lst; then
	echo "HYPH es PE hyph_es" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*es[ \t]*PR[ \t]*hyph_es" %{dictdir}/dictionary.lst; then
	echo "HYPH es PR hyph_es" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*es[ \t]*UY[ \t]*hyph_es" %{dictdir}/dictionary.lst; then
	echo "HYPH es UY hyph_es" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*es[ \t]*VE[ \t]*hyph_es" %{dictdir}/dictionary.lst; then
	echo "HYPH es VE hyph_es" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-hyph-es
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^HYPH.*es.*AR.*hyph_es$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^HYPH.*es.*BZ.*hyph_es$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^HYPH.*es.*BO.*hyph_es$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^HYPH.*es.*CL.*hyph_es$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^HYPH.*es.*CO.*hyph_es$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^HYPH.*es.*CR.*hyph_es$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^HYPH.*es.*CU.*hyph_es$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^HYPH.*es.*DO.*hyph_es$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^HYPH.*es.*EC.*hyph_es$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^HYPH.*es.*ES.*hyph_es$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^HYPH.*es.*GU.*hyph_es$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^HYPH.*es.*JN.*hyph_es$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^HYPH.*es.*MX.*hyph_es$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^HYPH.*es.*NI.*hyph_es$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^HYPH.*es.*PA.*hyph_es$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^HYPH.*es.*PU.*hyph_es$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^HYPH.*es.*PE.*hyph_es$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^HYPH.*es.*PR.*hyph_es$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^HYPH.*es.*SV.*hyph_es$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^HYPH.*es.*UY.*hyph_es$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^HYPH.*es.*VE.*hyph_es$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-hyph-et
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*et[ \t]*EE[ \t]*hyph_et_EE" %{dictdir}/dictionary.lst; then
	umask 002
	echo "HYPH et EE hyph_et_EE" >> %{dictdir}/dictionary.lst
fi
%preun -n myspell-hyph-et
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^HYPH.*et.*EE.*hyph_et_EE$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-hyph-fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*fi[ \t]*FI[ \t]*hyph_fi_FI" %{dictdir}/dictionary.lst; then
	umask 002
	echo "HYPH fi FI hyph_fi_FI" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-hyph-fi
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^HYPH.*fi.*FI.*hyph_fi_FI$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-hyph-fr
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*fr[ \t]*FR[ \t]*hyph_fr" %{dictdir}/dictionary.lst; then
	echo "HYPH fr FR hyph_fr" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*fr[ \t]*BE[ \t]*hyph_fr" %{dictdir}/dictionary.lst; then
	echo "HYPH fr BE hyph_fr" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*fr[ \t]*CA[ \t]*hyph_fr" %{dictdir}/dictionary.lst; then
	echo "HYPH fr CA hyph_fr" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*fr[ \t]*LU[ \t]*hyph_fr" %{dictdir}/dictionary.lst; then
	echo "HYPH fr LU hyph_fr" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*fr[ \t]*MC[ \t]*hyph_fr" %{dictdir}/dictionary.lst; then
	echo "HYPH fr MC hyph_fr" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*fr[ \t]*CH[ \t]*hyph_fr" %{dictdir}/dictionary.lst; then
	echo "HYPH fr CH hyph_fr" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-hyph-fr
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^HYPH.*fr.*BE.*hyph_fr$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^HYPH.*fr.*CA.*hyph_fr$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^HYPH.*fr.*CH.*hyph_fr$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^HYPH.*fr.*FR.*hyph_fr$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^HYPH.*fr.*LU.*hyph_fr$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^HYPH.*fr.*MC.*hyph_fr$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-hyph-ga
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*ga[ \t]*IE[ \t]*hyph_ga_IE" %{dictdir}/dictionary.lst; then
	umask 002
	echo "HYPH ga IE hyph_ga_IE" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-hyph-ga
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^HYPH.*ga.*IE.*hyph_ga_IE$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-hyph-hu
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*hu[ \t]*HU[ \t]*hyph_hu" %{dictdir}/dictionary.lst; then
	umask 002
	echo "HYPH hu HU hyph_hu" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-hyph-hu
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^HYPH.*hu.*HU.*hyph_hu$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-hyph-ia
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*ia[ \t]*IA[ \t]*hyph_ia" %{dictdir}/dictionary.lst; then
	umask 002
	echo "HYPH ia IA hyph_ia" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-hyph-ia
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^HYPH.*ia.*IA.*hyph_ia$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-hyph-id
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*id[ \t]*ID[ \t]*hyph_id_ID" %{dictdir}/dictionary.lst; then
	umask 002
	echo "HYPH id ID hyph_id_ID" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-hyph-id
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^HYPH.*id.*ID.*hyph_id_ID$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-hyph-is
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*is[ \t]*IS[ \t]*hyph_is_IS" %{dictdir}/dictionary.lst; then
	umask 002
	echo "HYPH is IS hyph_is_IS" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-hyph-is
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^HYPH.*is.*IS.*hyph_is_IS$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-hyph-it
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*it[ \t]*IT[ \t]*hyph_it" %{dictdir}/dictionary.lst; then
	echo "HYPH it IT hyph_it" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*it[ \t]*CH[ \t]*hyph_it" %{dictdir}/dictionary.lst; then
	echo "HYPH it CH hyph_it" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-hyph-it
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^HYPH.*it.*CH.*hyph_it$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^HYPH.*it.*IT.*hyph_it$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-hyph-lt
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*lt[ \t]*LT[ \t]*hyph_lt_LT" %{dictdir}/dictionary.lst; then
	umask 002
	echo "HYPH lt LT hyph_lt_LT" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-hyph-lt
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^HYPH.*lt.*LT.*hyph_lt_LT$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-hyph-lv
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*lv[ \t]*LV[ \t]*hyph_lv_LV" %{dictdir}/dictionary.lst; then
	umask 002
	echo "HYPH lv LV hyph_lv_LV" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-hyph-lv
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^HYPH.*lv.*LV.*hyph_lv_LV$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-hyph-nl
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*nl[ \t]*NL[ \t]*hyph_nl" %{dictdir}/dictionary.lst; then
	umask 002
	echo "HYPH nl NL hyph_nl" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-hyph-nl
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^HYPH.*nl.*NL.*hyph_nl$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-hyph-pl
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*pl[ \t]*PL[ \t]*hyph_pl_PL" %{dictdir}/dictionary.lst; then
	umask 002
	echo "HYPH pl PL hyph_pl_PL" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-hyph-pl
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^HYPH.*pl.*PL.*hyph_pl_PL$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-hyph-pt
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*pt[ \t]*PT[ \t]*hyph_pt" %{dictdir}/dictionary.lst; then
	umask 002
	echo "HYPH pt PT hyph_pt" >> %{dictdir}/dictionary.lst
fi

if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*pt[ \t]*BR[ \t]*hyph_pt" %{dictdir}/dictionary.lst; then
	echo "HYPH pt BR hyph_pt" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-hyph-pt
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^HYPH.*pt.*BR.*hyph_pt$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^HYPH.*pt.*PT.*hyph_pt$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-hyph-ru
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*ru[ \t]*RU[ \t]*hyph_ru_RU" %{dictdir}/dictionary.lst; then
	umask 002
	echo "HYPH ru RU hyph_ru_RU" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-hyph-ru
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^HYPH.*ru.*RU.*hyph_ru_RU$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-hyph-sk
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*sk[ \t]*SK[ \t]*hyph_sk_SK" %{dictdir}/dictionary.lst; then
	umask 002
	echo "HYPH sk SK hyph_sk_SK" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-hyph-sk
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^HYPH.*sk.*SK.*hyph_sk_SK$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-hyph-sl
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*sl[ \t]*SI[ \t]*hyph_sl_SI" %{dictdir}/dictionary.lst; then
	umask 002
	echo "HYPH sl SI hyph_sl_SI" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-hyph-sl
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^HYPH.*sl.*SI.*hyph_sl_SI$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-hyph-sv
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*sv[ \t]*SE[ \t]*hyph_sv_SE" %{dictdir}/dictionary.lst; then
	umask 002
	echo "HYPH sv SE hyph_sv_SE" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-hyph-sv
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^HYPH.*sv.*SE.*hyph_sv_SE$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-hyph-uk
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*uk[ \t]*UA[ \t]*hyph_uk_UA" %{dictdir}/dictionary.lst; then
	umask 002
	echo "HYPH uk UA hyph_uk_UA" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-hyph-uk
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^HYPH.*uk.*UA.*hyph_uk_UA$/d' %{dictdir}/dictionary.lst
fi

##
## Scripts for thesaurus
##
%post -n myspell-thes-bg_BG
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^THES[ \t]*bg[ \t]*BG[ \t]*th_bg_BG" %{dictdir}/dictionary.lst; then
	umask 002
	echo "THES bg BG th_bg_BG" >> %{dictdir}/dictionary.lst
fi
%preun -n myspell-thes-bg_BG
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^THES.*bg.*BG.*th_bg_BG$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-thes-de_DE
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^THES[ \t]*de[ \t]*DE[ \t]*th_de_DE" %{dictdir}/dictionary.lst; then
	umask 002
	echo "THES de DE th_de_DE" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^THES[ \t]*de[ \t]*AT[ \t]*th_de_DE" %{dictdir}/dictionary.lst; then
	echo "THES de AT th_de_DE" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^THES[ \t]*de[ \t]*CH[ \t]*th_de_DE" %{dictdir}/dictionary.lst; then
	echo "THES de CH th_de_DE" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^THES[ \t]*de[ \t]*LI[ \t]*th_de_DE" %{dictdir}/dictionary.lst; then
	echo "THES de LI th_de_DE" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^THES[ \t]*de[ \t]*LU[ \t]*th_de_DE" %{dictdir}/dictionary.lst; then
	echo "THES de LU th_de_DE" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-thes-de_DE
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^THES.*de.*AT.*th_de_DE$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^THES.*de.*CH.*th_de_DE$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^THES.*de.*DE.*th_de_DE$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^THES.*de.*LI.*th_de_DE$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^THES.*de.*LU.*th_de_DE$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-thes-en_US
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^THES[ \t]*en[ \t]*US[ \t]*th_en_US" %{dictdir}/dictionary.lst; then
	echo "THES en US th_en_US" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^THES[ \t]*en[ \t]*CA[ \t]*th_en_US" %{dictdir}/dictionary.lst; then
	echo "THES en CA th_en_US" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^THES[ \t]*en[ \t]*GB[ \t]*th_en_US" %{dictdir}/dictionary.lst; then
	echo "THES en GB th_en_US" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^THES[ \t]*en[ \t]*AU[ \t]*th_en_US" %{dictdir}/dictionary.lst; then
	echo "THES en AU th_en_US" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^THES[ \t]*en[ \t]*BZ[ \t]*th_en_US" %{dictdir}/dictionary.lst; then
	echo "THES en BZ th_en_US" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^THES[ \t]*en[ \t]*IE[ \t]*th_en_US" %{dictdir}/dictionary.lst; then
	echo "THES en IE th_en_US" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^THES[ \t]*en[ \t]*JM[ \t]*th_en_US" %{dictdir}/dictionary.lst; then
	echo "THES en JM th_en_US" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^THES[ \t]*en[ \t]*NZ[ \t]*th_en_US" %{dictdir}/dictionary.lst; then
	echo "THES en NZ th_en_US" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^THES[ \t]*en[ \t]*PH[ \t]*th_en_US" %{dictdir}/dictionary.lst; then
	echo "THES en PH th_en_US" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^THES[ \t]*en[ \t]*TT[ \t]*th_en_US" %{dictdir}/dictionary.lst; then
	echo "THES en TT th_en_US" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^THES[ \t]*en[ \t]*ZA[ \t]*th_en_US" %{dictdir}/dictionary.lst; then
	echo "THES en ZA th_en_US" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^THES[ \t]*en[ \t]*ZW[ \t]*th_en_US" %{dictdir}/dictionary.lst; then
	echo "THES en ZW th_en_US" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-thes-en_US
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^THES.*en.*AU.*th_en_US$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^THES.*en.*BZ.*th_en_US$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^THES.*en.*CA.*th_en_US$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^THES.*en.*GB.*th_en_US$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^THES.*en.*IE.*th_en_US$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^THES.*en.*JM.*th_en_US$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^THES.*en.*NZ.*th_en_US$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^THES.*en.*PH.*th_en_US$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^THES.*en.*TT.*th_en_US$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^THES.*en.*US.*th_en_US$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^THES.*en.*ZA.*th_en_US$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^THES.*en.*ZW.*th_en_US$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-thes-es_ES
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^THES[ \t]*es[ \t]*ES[ \t]*th_es_ES" %{dictdir}/dictionary.lst; then
	echo "THES es ES th_es_ES" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^THES[ \t]*es[ \t]*AR[ \t]*th_es_ES" %{dictdir}/dictionary.lst; then
	echo "THES es AR th_es_ES" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-thes-es_ES
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^THES.*es.*AR.*th_es_ES$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^THES.*es.*ES.*th_es_ES$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-thes-fr_FR
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^THES[ \t]*fr[ \t]*FR[ \t]*th_fr_FR" %{dictdir}/dictionary.lst; then
	echo "THES fr FR th_fr_FR" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^THES[ \t]*fr[ \t]*BE[ \t]*th_fr_FR" %{dictdir}/dictionary.lst; then
	echo "THES fr BE th_fr_FR" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^THES[ \t]*fr[ \t]*CA[ \t]*th_fr_FR" %{dictdir}/dictionary.lst; then
	echo "THES fr CA th_fr_FR" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^THES[ \t]*fr[ \t]*CH[ \t]*th_fr_FR" %{dictdir}/dictionary.lst; then
	echo "THES fr CH th_fr_FR" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^THES[ \t]*fr[ \t]*LU[ \t]*th_fr_FR" %{dictdir}/dictionary.lst; then
	echo "THES fr LU th_fr_FR" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^THES[ \t]*fr[ \t]*MC[ \t]*th_fr_FR" %{dictdir}/dictionary.lst; then
	echo "THES fr MC th_fr_FR" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-thes-fr_FR
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^THES.*fr.*BE.*th_fr_FR$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^THES.*fr.*CA.*th_fr_FR$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^THES.*fr.*CH.*th_fr_FR$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^THES.*fr.*FR.*th_fr_FR$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^THES.*fr.*LU.*th_fr_FR$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^THES.*fr.*MC.*th_fr_FR$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-thes-it_IT
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^THES[ \t]*it[ \t]*CH[ \t]*th_it_IT" %{dictdir}/dictionary.lst; then
	echo "THES it CH th_it_IT" >> %{dictdir}/dictionary.lst
fi
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^THES[ \t]*it[ \t]*IT[ \t]*th_it_IT" %{dictdir}/dictionary.lst; then
	echo "THES it IT th_it_IT" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-thes-it_IT
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^THES.*it.*CH.*th_it_IT$/d' %{dictdir}/dictionary.lst
	%{__sed} -i -e '/^THES.*it.*IT.*th_it_IT$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-thes-pl_PL
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^THES[ \t]*pl[ \t]*PL[ \t]*th_pl_PL" %{dictdir}/dictionary.lst; then
	umask 002
	echo "THES pl PL th_pl_PL" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-thes-pl_PL
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^THES.*pl.*PL.*th_pl_PL$/d' %{dictdir}/dictionary.lst
fi

%post -n myspell-thes-sk_SK
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^THES[ \t]*sk[ \t]*SK[ \t]*th_sk_SK" %{dictdir}/dictionary.lst; then
	umask 002
	echo "THES sk SK th_sk_SK" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-thes-sk_SK
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^THES.*sk.*SK.*th_sk_SK$/d' %{dictdir}/dictionary.lst
fi

%files -n myspell-common
%defattr(644,root,root,755)
%dir %{dictdir}
%config(noreplace) %verify(not md5 mtime size) %{dictdir}/dictionary.lst

##
## Files for spell checking
##
%files -n myspell-af_ZA
%defattr(644,root,root,755)
%doc doc/DICT/af_ZA/*
%{dictdir}/af_ZA.*

%files -n myspell-bg_BG
%defattr(644,root,root,755)
%doc doc/DICT/bg_BG/*
%{dictdir}/bg_BG.*

%files -n myspell-ca_ES
%defattr(644,root,root,755)
%doc doc/DICT/ca_ES/*
%{dictdir}/ca_ES.*

%files -n myspell-cs_CZ
%defattr(644,root,root,755)
%doc doc/DICT/cs_CZ/*
%{dictdir}/cs_CZ.*

%files -n myspell-cy_GB
%defattr(644,root,root,755)
%doc doc/DICT/cy_GB/*
%{dictdir}/cy_GB.*

%files -n myspell-da_DK
%defattr(644,root,root,755)
%doc doc/DICT/da_DK/*
%{dictdir}/da_DK.*

%files -n myspell-de_AT
%defattr(644,root,root,755)
%doc doc/DICT/de_AT/*
%{dictdir}/de_AT.*

%files -n myspell-de_CH
%defattr(644,root,root,755)
%doc doc/DICT/de_CH/*
%{dictdir}/de_CH.*

%files -n myspell-de_DE
%defattr(644,root,root,755)
%doc doc/DICT/de_DE/*
%{dictdir}/de_DE.*

%files -n myspell-el_GR
%defattr(644,root,root,755)
%doc doc/DICT/el_GR/*
%{dictdir}/el_GR.*

%files -n myspell-en_AU
%defattr(644,root,root,755)
%doc doc/DICT/en_AU/*
%{dictdir}/en_AU.*

%files -n myspell-en_CA
%defattr(644,root,root,755)
%doc doc/DICT/en_CA/*
%{dictdir}/en_CA.*

%files -n myspell-en_GB
%defattr(644,root,root,755)
%doc doc/DICT/en_GB/*
%{dictdir}/en_GB.*

%files -n myspell-en_NZ
%defattr(644,root,root,755)
%doc doc/DICT/en_NZ/*
%{dictdir}/en_NZ.*

%files -n myspell-en_US
%defattr(644,root,root,755)
%doc doc/DICT/en_US/*
%{dictdir}/en_US.*

%files -n myspell-es_ES
%defattr(644,root,root,755)
%doc doc/DICT/es_ES/*
%{dictdir}/es_ES.*

%files -n myspell-es_MX
%defattr(644,root,root,755)
%doc doc/DICT/es_MX/*
%{dictdir}/es_MX.*

%files -n myspell-et_EE
%defattr(644,root,root,755)
%doc doc/DICT/et_EE/*
%{dictdir}/et_EE.*

%files -n myspell-fo_FO
%defattr(644,root,root,755)
%doc doc/DICT/fo_FO/*
%{dictdir}/fo_FO.*

%files -n myspell-fr_BE
%defattr(644,root,root,755)
%doc doc/DICT/fr_BE/*
%{dictdir}/fr_BE.*

%files -n myspell-fr_FR
%defattr(644,root,root,755)
%doc doc/DICT/fr_FR/*
%{dictdir}/fr_FR.*

%files -n myspell-ga_IE
%defattr(644,root,root,755)
%doc doc/DICT/ga_IE/*
%{dictdir}/ga_IE.*

%files -n myspell-gl_ES
%defattr(644,root,root,755)
%doc doc/DICT/gl_ES/*
%{dictdir}/gl_ES.*

%files -n myspell-he_IL
%defattr(644,root,root,755)
%doc doc/DICT/he_IL/*
%{dictdir}/he_IL.*

%files -n myspell-hr_HR
%defattr(644,root,root,755)
%doc doc/DICT/hr_HR/*
%{dictdir}/hr_HR.*

%files -n myspell-hu_HU
%defattr(644,root,root,755)
%doc doc/DICT/hu_HU/*
%{dictdir}/hu_HU.*

%files -n myspell-ia_IA
%defattr(644,root,root,755)
%doc doc/DICT/ia_IA/*
%{dictdir}/ia_IA.*

%files -n myspell-id_ID
%defattr(644,root,root,755)
%doc doc/DICT/id_ID/*
%{dictdir}/id_ID.*

%files -n myspell-it_IT
%defattr(644,root,root,755)
%doc doc/DICT/it_IT/*
%{dictdir}/it_IT.*

%files -n myspell-la_VA
%defattr(644,root,root,755)
%doc doc/DICT/la_VA/*
%{dictdir}/la_VA.*

%files -n myspell-lt_LT
%defattr(644,root,root,755)
%doc doc/DICT/lt_LT/*
%{dictdir}/lt_LT.*

%files -n myspell-lv_LV
%defattr(644,root,root,755)
%doc doc/DICT/lv_LV/*
%{dictdir}/lv_LV.*

%files -n myspell-mi_NZ
%defattr(644,root,root,755)
%doc doc/DICT/mi_NZ/*
%{dictdir}/mi_NZ.*

%files -n myspell-ms_MY
%defattr(644,root,root,755)
%doc doc/DICT/ms_MY/*
%{dictdir}/ms_MY.*

%files -n myspell-nb_NO
%defattr(644,root,root,755)
%doc doc/DICT/nb_NO/*
%{dictdir}/nb_NO.*

%files -n myspell-nl_NL
%defattr(644,root,root,755)
%doc doc/DICT/nl_NL/*
%{dictdir}/nl_NL.*

%files -n myspell-nn_NO
%defattr(644,root,root,755)
%doc doc/DICT/nn_NO/*
%{dictdir}/nn_NO.*

%files -n myspell-pl_PL
%defattr(644,root,root,755)
%doc doc/DICT/pl_PL/*
%{dictdir}/pl_PL.*

%files -n myspell-pt_BR
%defattr(644,root,root,755)
%doc doc/DICT/pt_BR/*
%{dictdir}/pt_BR.*

%files -n myspell-pt_PT
%defattr(644,root,root,755)
%doc doc/DICT/pt_PT/*
%{dictdir}/pt_PT.*

%files -n myspell-ro_RO
%defattr(644,root,root,755)
%doc doc/DICT/ro_RO/*
%{dictdir}/ro_RO.*

%files -n myspell-ru_RU
%defattr(644,root,root,755)
%doc doc/DICT/ru_RU/*
%{dictdir}/ru_RU.*

%files -n myspell-sk_SK
%defattr(644,root,root,755)
%doc doc/DICT/sk_SK/*
%{dictdir}/sk_SK.*

%files -n myspell-sl_SI
%defattr(644,root,root,755)
%doc doc/DICT/sl_SI/*
%{dictdir}/sl_SI.*

%files -n myspell-sv_SE
%defattr(644,root,root,755)
%doc doc/DICT/sv_SE/*
%{dictdir}/sv_SE.*

%files -n myspell-sw_KE
%defattr(644,root,root,755)
%doc doc/DICT/sw_KE/*
%{dictdir}/sw_KE.*

%files -n myspell-uk_UA
%defattr(644,root,root,755)
%doc doc/DICT/uk_UA/*
%{dictdir}/uk_UA.*

%files -n myspell-zu_ZA
%defattr(644,root,root,755)
%doc doc/DICT/zu_ZA/*
%{dictdir}/zu_ZA.*

#
# Files for hyphenation
#

%files -n myspell-hyph-bg
%defattr(644,root,root,755)
%doc doc/HYPH/hyph_bg_BG/*
%{dictdir}/hyph_bg_BG.*

%files -n myspell-hyph-cs
%defattr(644,root,root,755)
%doc doc/HYPH/hyph_cs_CZ/*
%{dictdir}/hyph_cs_CZ.*

%files -n myspell-hyph-da
%defattr(644,root,root,755)
%doc doc/HYPH/hyph_da_DK/*
%{dictdir}/hyph_da_DK.*

%files -n myspell-hyph-de
%defattr(644,root,root,755)
%doc doc/HYPH/hyph_de/*
%{dictdir}/hyph_de.*

%files -n myspell-hyph-el
%defattr(644,root,root,755)
%doc doc/HYPH/hyph_el_GR/*
%{dictdir}/hyph_el_GR.*

%files -n myspell-hyph-en
%defattr(644,root,root,755)
%doc doc/HYPH/hyph_en/*
%{dictdir}/hyph_en.*

%files -n myspell-hyph-es
%defattr(644,root,root,755)
%doc doc/HYPH/hyph_es/*
%{dictdir}/hyph_es.*

%files -n myspell-hyph-et
%defattr(644,root,root,755)
%doc doc/HYPH/hyph_et_EE/*
%{dictdir}/hyph_et_EE.*

%files -n myspell-hyph-fi
%defattr(644,root,root,755)
%doc doc/HYPH/hyph_fi_FI/*
%{dictdir}/hyph_fi_FI.*

%files -n myspell-hyph-fr
%defattr(644,root,root,755)
%doc doc/HYPH/hyph_fr/*
%{dictdir}/hyph_fr.*

%files -n myspell-hyph-ga
%defattr(644,root,root,755)
%doc doc/HYPH/hyph_ga_IE/*
%{dictdir}/hyph_ga_IE.*

%files -n myspell-hyph-hu
%defattr(644,root,root,755)
%doc doc/HYPH/hyph_hu/*
%{dictdir}/hyph_hu.*

%files -n myspell-hyph-ia
%defattr(644,root,root,755)
%doc doc/HYPH/hyph_ia/*
%{dictdir}/hyph_ia.*

%files -n myspell-hyph-id
%defattr(644,root,root,755)
%doc doc/HYPH/hyph_id_ID/*
%{dictdir}/hyph_id_ID.*

%files -n myspell-hyph-is
%defattr(644,root,root,755)
%doc doc/HYPH/hyph_is_IS/*
%{dictdir}/hyph_is_IS.*

%files -n myspell-hyph-it
%defattr(644,root,root,755)
%doc doc/HYPH/hyph_it/*
%{dictdir}/hyph_it.*

%files -n myspell-hyph-lt
%defattr(644,root,root,755)
%doc doc/HYPH/hyph_lt_LT/*
%{dictdir}/hyph_lt_LT.*

%files -n myspell-hyph-lv
%defattr(644,root,root,755)
%doc doc/HYPH/hyph_lv_LV/*
%{dictdir}/hyph_lv_LV.*

%files -n myspell-hyph-nl
%defattr(644,root,root,755)
%doc doc/HYPH/hyph_nl/*
%{dictdir}/hyph_nl.*

%files -n myspell-hyph-pl
%defattr(644,root,root,755)
%doc doc/HYPH/hyph_pl_PL/*
%{dictdir}/hyph_pl_PL.*

%files -n myspell-hyph-pt
%defattr(644,root,root,755)
%doc doc/HYPH/hyph_pt/*
%{dictdir}/hyph_pt.*

%files -n myspell-hyph-ru
%defattr(644,root,root,755)
%doc doc/HYPH/hyph_ru_RU/*
%{dictdir}/hyph_ru_RU.*

%files -n myspell-hyph-sk
%defattr(644,root,root,755)
%doc doc/HYPH/hyph_sk_SK/*
%{dictdir}/hyph_sk_SK.*

%files -n myspell-hyph-sl
%defattr(644,root,root,755)
%doc doc/HYPH/hyph_sl_SI/*
%{dictdir}/hyph_sl_SI.*

%files -n myspell-hyph-sv
%defattr(644,root,root,755)
%doc doc/HYPH/hyph_sv_SE/*
%{dictdir}/hyph_sv_SE.*

%files -n myspell-hyph-uk
%defattr(644,root,root,755)
%doc doc/HYPH/hyph_uk_UA/*
%{dictdir}/hyph_uk_UA.*

#
# Files for thesaurus
#

%files -n myspell-thes-bg_BG
%defattr(644,root,root,755)
%doc doc/THES/th_bg_BG/*
%{dictdir}/th_bg_BG.*

%files -n myspell-thes-de_DE
%defattr(644,root,root,755)
%doc doc/THES/th_de_DE/*
%{dictdir}/th_de_DE.*

%files -n myspell-thes-en_US
%defattr(644,root,root,755)
%doc doc/THES/th_en_US/*
%{dictdir}/th_en_US.*

%files -n myspell-thes-es_ES
%defattr(644,root,root,755)
%doc doc/THES/th_es_ES/*
%{dictdir}/th_es_ES.*

%files -n myspell-thes-fr_FR
%defattr(644,root,root,755)
%doc doc/THES/th_fr_FR/*
%{dictdir}/th_fr_FR.*

%files -n myspell-thes-it_IT
%defattr(644,root,root,755)
%doc doc/THES/th_it_IT/*
%{dictdir}/th_it_IT.*

%files -n myspell-thes-pl_PL
%defattr(644,root,root,755)
%doc doc/THES/th_pl_PL/*
%{dictdir}/th_pl_PL.*

%files -n myspell-thes-sk_SK
%defattr(644,root,root,755)
%doc doc/THES/th_sk_SK/*
%{dictdir}/th_sk_SK.*

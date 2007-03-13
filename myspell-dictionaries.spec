# TODO
# - add dictionaries currently obsoleted in -common
# - merge (compare) changes with mozilla-thunderbird-dictionary-* (on Attic) and myspell-common Obsoletes
#
%define		_ver	1.0.2
%define		_rel	2
Summary:	MySpell Spelling and Hyphenation dictionaries
Name:		myspell-dictionaries
Version:	%{_ver}
Release:	%{_rel}
License:	BSD/GPL/LGPL
Group:		Applications/Text
URL:		http://lingucomponent.openoffice.org/download_dictionary.html
## Sources for spell checking dictionaries
Source100:	bg_BG.zip
# Source100-md5:	0619620e36b1a9a45995f939d765fd3e
Source101:	ca_ES.zip
# Source101-md5:	6cea81b3e1101fb277062e7eef4ff720
Source102:	hr_HR.zip
# Source102-md5:	5c5d0479b0fb7e7d2b5e0533cc2e370b
Source103:	cs_CZ.zip
# Source103-md5:	b8d4a6943ec18300a9b0047d2540209e
Source104:	da_DK.zip
# Source104-md5:	8d3df34ef13c54f8f112dcb23d7b2b49
Source105:	nl_NL.zip
# Source105-md5:	caab73fe1aaf03a59860765e0b7637f8
Source106:	en_CA.zip
# Source106-md5:	c14942ea471a5182f376802c68933880
Source107:	en_GB.zip
# Source107-md5:	31736e7e88a2cc94e17ac7d9b1ad580f
Source108:	en_US.zip
# Source108-md5:	21f03b559933dc11688a2aa85359902b
Source109:	fr_FR.zip
# Source109-md5:	904d799ab36df32cc598a8dc7990649f
Source110:	de_DE.zip
# Source110-md5:	9eb02aad372bcd12209e761762ffb10a
Source111:	de_CH.zip
# Source111-md5:	2da60dd02b5a62f1a5c8b9e4a3a7fe4d
Source112:	el_GR.zip
# Source112-md5:	86e612d5cc243bdd0f09c919c9487c64
Source113:	hu_HU.zip
# Source113-md5:	e697bbd1025a7f11716d7988fcfba778
Source114:	it_IT.zip
# Source114-md5:	87f74209b5422efd9a82c97f2063b19e
# From http://www.kurnik.pl/dictionary/alt-myspell-pl-20060823.tar.bz2
Source115:	pl_PL.zip
# Source115-md5:	b5fc0ebe5a455e337bdcfeef213cf706
#Source115:	http://www.kurnik.pl/dictionary/alt-myspell-pl-20060823.tar.bz2
Source116:	pt_PT.zip
# Source116-md5:	6f44ed7caf6846dca9d539bb390719c4
Source117:	pt_BR.zip
# Source117-md5:	83aa4540283c0049c27271576890fd88
Source118:	es_ES.zip
# Source118-md5:	2e99ae081d37b87536452327e71c2d13
Source119:	sk_SK.zip
# Source119-md5:	2cd6e4e2fe7558fe98053b1cb103215d
Source120:	sv_SE.zip
# Source120-md5:	8d9c49a43bfbecec6962c1344914dc8d
Source121:	nb_NO.zip
# Source121-md5:	8868ade2fae74e7c07f6f30479e654d1
Source122:	nn_NO.zip
# Source122-md5:	9a2826b88207e25135caa8481bebf5ad
Source123:	ga_IE.zip
# Source123-md5:	c2d63e41c2e72f5498cbe4f6266043a1
Source124:	gl_ES.zip
# Source124-md5:	7270162479a5efc8e6acdc61d625fa26
Source125:	ru_RU.zip
# Source125-md5:	67da1e4d594de554a9184568235ab301
Source126:	sl_SI.zip
# Source126-md5:	a79c19d16bc26349bbded16b410616a8
Source127:	uk_UA.zip
# Source127-md5:	a0ae3b331ae5566a330d1bccc4a95791
Source128:	de_AT.zip
# Source128-md5:	fdee257cc4e9d49968048a6e3edec91a
Source129:	en_AU.zip
# Source129-md5:	c39f529173d8bb0e15b1fade11dfe780
Source130:	es_MX.zip
# Source130-md5:	1a8b2d34033f3d4c8e51892084e9d6fa
Source131:	fo_FO.zip
# Source131-md5:	647b7b31d02fbdb33f4f309a5da4b838
Source132:	fr_BE.zip
# Source132-md5:	a7ac4f1e3f61f2e96595f7d5614fcafc
Source133:	lt_LT.zip
# Source133-md5:	3590ba02288c9092340101dca3ddc132
Source134:	ftp://ftp.linux.ee/pub/openoffice/contrib/dictionaries/et_EE.zip
# Source134-md5:	2a1e97d61132c537aa03df4d0fee9b89
# http://sourceforge.net/project/showfiles.php?group_id=91920
#Source135:	http://dl.sourceforge.net/translate/myspell-af_ZA-20060117.zip
Source135:	af_ZA.zip
# Source135-md5:	44a526eb5005fde76c964e4180d47f3f
Source136:	cy_GB.zip
# Source136-md5:	accdb94f38555af45a54494e046a88f3
Source137:	en_NZ.zip
# Source137-md5:	8ac9e6640d132de29571f81d33012bb8
Source138:	id_ID.zip
# Source138-md5:	fe0ac356fd725cf1d5197e040fb507fc
Source139:	zu_ZA.zip
# Source139-md5:	1208ce6b26b3023da5210fad50d6e47a
Source140:	ro_RO.zip
# Source140-md5:	c8a56b8d79450dcb3ca68c6987da1930
Source141:	mi_NZ.zip
# Source141-md5:	f691ca67df4570821f931574295715b5
Source142:	sw_KE.zip
# Source142-md5:	af1bb4afd5e46e3624a785d1323ee6a7
Source143:	ms_MY.zip
# Source143-md5:	f1db7ff9dd8be247e1bca30042dba115
## Sources for hyphenation dictionaries
Source200:	hyph_da.zip
# Source200-md5:	647cb755de87e55f36b6819c88ca928b
Source201:	hyph_en.zip
# Source201-md5:	aadf421e4e17c90c9dd72c39e230aa68
Source202:	hyph_fr.zip
# Source202-md5:	00f8a2a219b2eb7b6a4ed56c634c3988
Source203:	hyph_de.zip
# Source203-md5:	ac783ca0316247d40c656d4c79035865
Source204:	hyph_it.zip
# Source204-md5:	ed30e249947bc1522a193cc12166be1f
Source205:	hyph_ru.zip
# Source205-md5:	1c0e92f62496c6477fa5112f99e1074d
Source206:	hyph_nl.zip
# Source206-md5:	cf4a9d3dd3e71c0939ffe014cf379134
Source207:	hyph_cs.zip
# Source207-md5:	b1cd60f130668ee363baf566ee93ab99
Source208:	hyph_es.zip
# Source208-md5:	02e10e9dcfed4965f932a3d800ff7ac9
Source209:	hyph_sk.zip
# Source209-md5:	62c7b806bab885de1ef51c69a91ab569
Source210:	hyph_sl.zip
# Source210-md5:	cc67d86781eae913c39d76cd9a12dce8
Source211:	hyph_uk.zip
# Source211-md5:	0e4e5c997cab91ae4e53dcd93d7735bf
Source212:	hyph_hu.zip
# Source212-md5:	c816d84cdf1ab63aa88b786c7723d7c0
Source213:	hyph_sv.zip
# Source213-md5:	a7af73dd84cc8f959f13853b4f8363a5
#Source214:	ftp://ftp.linux.ee/pub/openoffice/contrib/dictionaries/hyph_et_EE.zip
Source214:	hyph_et.zip
# Source214-md5:	866e01bd74b729be6fe09db075314007
Source215:	hyph_id.zip
# Source215-md5:	a98334abf10af82c9358e468010d34e4
Source216:	hyph_pl.zip
# Source216-md5:	7d836b3c154f156a0efa87b76e9dc26a
Source217:	hyph_pt.zip
# Source217-md5:	8b9abb106cf76c0df933b0d33847d961
Source218:	hyph_el.zip
# Source218-md5:	bc9ad651a4058aff93e35ceda21c35be
# See http://bgoffice.sourceforge.net/ooo/index.html
#Source219:	http://dl.sourceforge.net/bgoffice/OOo-hyph-bg-4.0.zip
Source219:	hyph_bg.zip
# Source219-md5:	90f50ccda0d8e0d95c4614d30a97722d
Source220:	hyph_lt.zip
# Source220-md5:	d1801298677d0e2e7e56702c7a0c406a
Source221:	hyph_is.zip
# Source221-md5:	d2a599bb65e607eedfcb8123d9016d03
Source222:	hyph_ga.zip
# Source222-md5:	23fb9ccc5d7193da8e7daaa34f00235c
Source223:	hyph_fi.zip
# Source223-md5:	df10e1430ab31d46e7afffb63598a3e4
Source300:	th_en_US.zip
# Source300-md5:	43c72a3bbc49759f2bd8c0870b097efe
Source301:	th_fr_FR.zip
# Source301-md5:	061d832c6a6537a61770d3e065e0b1bb
# http://it.openoffice.org/contribuire/thesaurus.html (alpha version!!!)
Source302:	th_it_IT.zip
# Source302-md5:	f8f06c860174e934ac7a7fb42d1f95dc
Source303:	th_de_DE.zip
# Source303-md5:	bb8de5610dd6f16d69193c7e689b081a
# http://synonimy.sourceforge.net/
Source304:	th_pl_PL.zip
# Source304-md5:	844dbb339719f07bed24e5bf4eda0436
#Source304:	http://dl.sourceforge.net/synonimy/OOo-Thesaurus-1.3.zip
Source305:	th_es_ES.zip
# Source305-md5:	6bf2f4bbca189d8c0976c84d835e2c72
## http://bgoffice.sourceforge.net/ooo/
Source306:	th_bg_BG.zip
# Source306-md5:	630ec215fcf655b99429ca7c97667b8d
#Source306:	http://dl.sourceforge.net/bgoffice/OOo-full-pack.zip
Source307:	th_sk_SK.zip
# Source307-md5:	df70385609f32d63a1e0d17712428755
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

%package -n myspell-common
Summary:	Common files for myspell and hunspell dictionaries
License:	Public Domain
Group:		Applications/Text
Provides:	mozilla-thunderbird-dictionary-he-IL
Provides:	mozilla-thunderbird-dictionary-ia
Provides:	mozilla-thunderbird-dictionary-la
Provides:	mozilla-thunderbird-dictionary-lv-LV
Provides:	mozilla-thunderbird-dictionary-ru-IE
Obsoletes:	mozilla-thunderbird-dictionary-he-IL
Obsoletes:	mozilla-thunderbird-dictionary-ia
Obsoletes:	mozilla-thunderbird-dictionary-la
Obsoletes:	mozilla-thunderbird-dictionary-lv-LV
Obsoletes:	mozilla-thunderbird-dictionary-ru-IE

%description -n myspell-common
Common files for myspell and hunspell dictionaries

# Spelling dictionaries
%package -n myspell-af_ZA
Summary:	MySpell spelling dictionaries for Afrikaans (Africa)
Version:	%{_ver}
Release:	0.20040727.%{_rel}
License:	LGPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	mozilla-thunderbird-dictionary-af-ZA
Provides:	myspell-af = %{version}
Provides:	myspell-dictionary = %{version}
Obsoletes:	mozilla-thunderbird-dictionary-af-ZA
Obsoletes:	myspell-af

%description -n myspell-af_ZA
myspell-af_ZA contains spell checking data in Afrikaans (Africa) to be
used by OpenOffice.org or MySpell-capable applications like Mozilla.
With this extension, you can compose a document in Afrikaans and check
for the typos easily.

%package -n myspell-bg_BG
Summary:	MySpell spelling dictionaries for Bulgarian (Bulgaria)
Version:	%{_ver}
Release:	0.20040402.%{_rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	mozilla-thunderbird-dictionary-bg
Provides:	myspell-bg = %{version}
Provides:	myspell-dictionary = %{version}
Obsoletes:	mozilla-thunderbird-dictionary-bg
Obsoletes:	myspell-bg

%description -n myspell-bg_BG
myspell-bg_BG contains spell checking data in Bulgarian (Bulgaria) to
be used by OpenOffice.org or MySpell-capable applications like
Mozilla. With this extension, you can compose a document in Bulgarian
and check for the typos easily.

%package -n myspell-ca_ES
Summary:	MySpell spelling dictionaries for Catalan
Version:	%{_ver}
Release:	0.20030907.%{_rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	mozilla-thunderbird-dictionary-ca
Provides:	myspell-ca = %{version}
Provides:	myspell-dictionary = %{version}
Obsoletes:	mozilla-thunderbird-dictionary-ca
Obsoletes:	myspell-ca

%description -n myspell-ca_ES
myspell-ca_ES contains spell checking data in Catalan to be used by
OpenOffice.org or MySpell-capable applications like Mozilla. With this
extension, you can compose a document in Catalan and check for the
typos easily.

%package -n myspell-cs_CZ
Summary:	MySpell spelling dictionaries for Czech (Czech Republic)
Version:	%{_ver}
Release:	0.20030907.%{_rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	mozilla-thunderbird-dictionary-cs
Provides:	myspell-cs = %{version}
Provides:	myspell-dictionary = %{version}
Obsoletes:	mozilla-thunderbird-dictionary-cs
Obsoletes:	myspell-cs

%description -n myspell-cs_CZ
myspell-cs_CZ contains spell checking data in Czech (Czech Republic)
to be used by OpenOffice.org or MySpell-capable applications like
Mozilla. With this extension, you can compose a document in Czech and
check for the typos easily.

%package -n myspell-cy_GB
Summary:	MySpell spelling dictionaries for Welsh (Wales)
Version:	%{_ver}
Release:	0.20040425.%{_rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	mozilla-thunderbird-dictionary-cy-GB
Provides:	myspell-cy = %{version}
Provides:	myspell-dictionary = %{version}
Obsoletes:	mozilla-thunderbird-dictionary-cy-GB
Obsoletes:	myspell-cy

%description -n myspell-cy_GB
myspell-cy_GB contains spell checking data in Welsh (Wales) to be used
by OpenOffice.org or MySpell-capable applications like Mozilla. With
this extension, you can compose a document in Welsh and check for the
typos easily.

%package -n myspell-da_DK
Summary:	MySpell spelling dictionaries for Danish (Denmark)
Version:	%{_ver}
Release:	0.20040609.%{_rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	mozilla-thunderbird-dictionary-da
Provides:	myspell-da = %{version}
Provides:	myspell-dictionary = %{version}
Obsoletes:	mozilla-thunderbird-dictionary-da
Obsoletes:	myspell-da

%description -n myspell-da_DK
myspell-da_DK contains spell checking data in Danish (Denmark) to be
used by OpenOffice.org or MySpell-capable applications like Mozilla.
With this extension, you can compose a document in Danish and check
for the typos easily.

%package -n myspell-de_AT
Summary:	MySpell spelling dictionaries for German (Austria)
Version:	%{_ver}
Release:	0.20030905.%{_rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	mozilla-thunderbird-dictionary-de-AT
Provides:	myspell-de = %{version}
Provides:	myspell-dictionary = %{version}
Obsoletes:	mozilla-thunderbird-dictionary-de-AT
Obsoletes:	myspell-de

%description -n myspell-de_AT
myspell-de_AT contains spell checking data in German (Austria) to be
used by OpenOffice.org or MySpell-capable applications like Mozilla.
With this extension, you can compose a document in German and check
for the typos easily.

%package -n myspell-de_CH
Summary:	MySpell spelling dictionaries for German (Switzerland)
Version:	%{_ver}
Release:	0.20030905.%{_rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	mozilla-thunderbird-dictionary-de-CH
Provides:	myspell-de = %{version}
Provides:	myspell-dictionary = %{version}
Obsoletes:	mozilla-thunderbird-dictionary-de-CH
Obsoletes:	myspell-de

%description -n myspell-de_CH
myspell-de_CH contains spell checking data in German (Switzerland) to
be used by OpenOffice.org or MySpell-capable applications like
Mozilla. With this extension, you can compose a document in German and
check for the typos easily.

%package -n myspell-de_DE
Summary:	MySpell spelling dictionaries for German (Germany)
Version:	%{_ver}
Release:	0.20030905.%{_rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	mozilla-thunderbird-dictionary-de-DE
Provides:	myspell-de = %{version}
Provides:	myspell-dictionary = %{version}
Obsoletes:	mozilla-thunderbird-dictionary-de-DE
Obsoletes:	myspell-de

%description -n myspell-de_DE
myspell-de_DE contains spell checking data in German (Germany) to be
used by OpenOffice.org or MySpell-capable applications like Mozilla.
With this extension, you can compose a document in German and check
for the typos easily.

%package -n myspell-el_GR
Summary:	MySpell spelling dictionaries for Greek (Greece)
Version:	%{_ver}
Release:	0.20040424.%{_rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	mozilla-thunderbird-dictionary-el
Provides:	myspell-dictionary = %{version}
Provides:	myspell-el = %{version}
Obsoletes:	mozilla-thunderbird-dictionary-el
Obsoletes:	myspell-el

%description -n myspell-el_GR
myspell-el_GR contains spell checking data in Greek (Greece) to be
used by OpenOffice.org or MySpell-capable applications like Mozilla.
With this extension, you can compose a document in Greek and check for
the typos easily.

%package -n myspell-en_AU
Summary:	MySpell spelling dictionaries for English (Australian)
Version:	%{_ver}
Release:	0.20030329.%{_rel}
License:	LGPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	mozilla-thunderbird-dictionary-en-AU
Provides:	myspell-dictionary = %{version}
Provides:	myspell-en = %{version}
Obsoletes:	mozilla-thunderbird-dictionary-en-AU
Obsoletes:	myspell-en

%description -n myspell-en_AU
myspell-en_AU contains spell checking data in English (Australian) to
be used by OpenOffice.org or MySpell-capable applications like
Mozilla. With this extension, you can compose a document in English
and check for the typos easily.

%package -n myspell-en_CA
Summary:	MySpell spelling dictionaries for English (Canada)
Version:	%{_ver}
Release:	0.20020315.%{_rel}
License:	Public Domain
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	mozilla-thunderbird-dictionary-en-CA
Provides:	myspell-dictionary = %{version}
Provides:	myspell-en = %{version}
Obsoletes:	mozilla-thunderbird-dictionary-en-CA
Obsoletes:	myspell-en

%description -n myspell-en_CA
myspell-en_CA contains spell checking data in English (Canada) to be
used by OpenOffice.org or MySpell-capable applications like Mozilla.
With this extension, you can compose a document in English and check
for the typos easily.

%package -n myspell-en_GB
Summary:	MySpell spelling dictionaries for English (United Kingdom)
Version:	%{_ver}
Release:	0.20040208.%{_rel}
License:	LGPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	mozilla-thunderbird-dictionary-en-GB
Provides:	myspell-dictionary = %{version}
Provides:	myspell-en = %{version}
Obsoletes:	mozilla-thunderbird-dictionary-en-GB
Obsoletes:	myspell-en

%description -n myspell-en_GB
myspell-en_GB contains spell checking data in English (United Kingdom)
to be used by OpenOffice.org or MySpell-capable applications like
Mozilla. With this extension, you can compose a document in English
and check for the typos easily.

%package -n myspell-en_NZ
Summary:	MySpell spelling dictionaries for English (New Zealand)
Version:	%{_ver}
Release:	0.20030907.%{_rel}
License:	LGPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	mozilla-thunderbird-dictionary-en-NZ
Provides:	myspell-dictionary = %{version}
Provides:	myspell-en = %{version}
Obsoletes:	mozilla-thunderbird-dictionary-en-NZ
Obsoletes:	myspell-en

%description -n myspell-en_NZ
myspell-en_NZ contains spell checking data in English (New Zealand) to
be used by OpenOffice.org or MySpell-capable applications like
Mozilla. With this extension, you can compose a document in English
and check for the typos easily.

%package -n myspell-en_US
Summary:	MySpell spelling dictionaries for English (US)
Version:	%{_ver}
Release:	0.20040623.%{_rel}
License:	BSD
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	mozilla-thunderbird-dictionary-en-US
Provides:	myspell-dictionary = %{version}
Provides:	myspell-en = %{version}
Obsoletes:	mozilla-thunderbird-dictionary-en-US
Obsoletes:	myspell-en

%description -n myspell-en_US
myspell-en_US contains spell checking data in English (US) to be used
by OpenOffice.org or MySpell-capable applications like Mozilla. With
this extension, you can compose a document in English and check for
the typos easily.

%package -n myspell-es_ES
Summary:	MySpell spelling dictionaries for Spanish (Spain)
Version:	%{_ver}
Release:	0.20040626.%{_rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	mozilla-thunderbird-dictionary-es-ES
Provides:	myspell-dictionary = %{version}
Provides:	myspell-es = %{version}
Obsoletes:	mozilla-thunderbird-dictionary-es-ES
Obsoletes:	myspell-es

%description -n myspell-es_ES
myspell-es_ES contains spell checking data in Spanish (Spain) to be
used by OpenOffice.org or MySpell-capable applications like Mozilla.
With this extension, you can compose a document in Spanish and check
for the typos easily.

%package -n myspell-es_MX
Summary:	MySpell spelling dictionaries for Spanish (Mexico)
Version:	%{_ver}
Release:	0.20030818.%{_rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	mozilla-thunderbird-dictionary-es-MX
Provides:	myspell-dictionary = %{version}
Provides:	myspell-es = %{version}
Obsoletes:	mozilla-thunderbird-dictionary-es-MX
Obsoletes:	myspell-es

%description -n myspell-es_MX
myspell-es_MX contains spell checking data in Spanish (Mexico) to be
used by OpenOffice.org or MySpell-capable applications like Mozilla.
With this extension, you can compose a document in Spanish and check
for the typos easily.

%package -n myspell-et_EE
Summary:	MySpell spelling dictionaries for Estonian (Estonia)
Version:	%{_ver}
Release:	0.20040621.%{_rel}
License:	free, see http://www.eki.ee/eki/licence.html
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	myspell-dictionary = %{version}
Provides:	myspell-et = %{version}
Obsoletes:	myspell-et

%description -n myspell-et_EE
myspell-et_EE contains spell checking data in Estonian (Estonia) to be
used by OpenOffice.org or MySpell-capable applications like Mozilla.
With this extension, you can compose a document in Estonian and check
for the typos easily.

%package -n myspell-fo_FO
Summary:	MySpell spelling dictionaries for Faroese (Faroe Islands)
Version:	%{_ver}
Release:	0.20040403.%{_rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	mozilla-thunderbird-dictionary-fo
Provides:	myspell-dictionary = %{version}
Provides:	myspell-fo = %{version}
Obsoletes:	mozilla-thunderbird-dictionary-fo
Obsoletes:	myspell-fo

%description -n myspell-fo_FO
myspell-fo_FO contains spell checking data in Faroese (Faroe Islands)
to be used by OpenOffice.org or MySpell-capable applications like
Mozilla. With this extension, you can compose a document in Faroese
and check for the typos easily.

%package -n myspell-fr_BE
Summary:	MySpell spelling dictionaries for French (Belgium)
Version:	%{_ver}
Release:	0.20030619.%{_rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	myspell-dictionary = %{version}
Provides:	myspell-fr = %{version}
Obsoletes:	myspell-fr

%description -n myspell-fr_BE
myspell-fr_BE contains spell checking data in French (Belgium) to be
used by OpenOffice.org or MySpell-capable applications like Mozilla.
With this extension, you can compose a document in French and check
for the typos easily.

%package -n myspell-fr_FR
Summary:	MySpell spelling dictionaries for French (France)
Version:	%{_ver}
Release:	0.20020608.%{_rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	myspell-dictionary = %{version}
Provides:	myspell-fr = %{version}
Obsoletes:	myspell-fr

%description -n myspell-fr_FR
myspell-fr_FR contains spell checking data in French (France) to be
used by OpenOffice.org or MySpell-capable applications like Mozilla.
With this extension, you can compose a document in French and check
for the typos easily.

%package -n myspell-ga_IE
Summary:	MySpell spelling dictionaries for Irish (Ireland)
Version:	%{_ver}
Release:	0.20040404.%{_rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	mozilla-thunderbird-dictionary-ga
Provides:	myspell-dictionary = %{version}
Provides:	myspell-ga = %{version}
Obsoletes:	mozilla-thunderbird-dictionary-ga
Obsoletes:	myspell-ga

%description -n myspell-ga_IE
myspell-ga_IE contains spell checking data in Irish (Ireland) to be
used by OpenOffice.org or MySpell-capable applications like Mozilla.
With this extension, you can compose a document in Irish and check for
the typos easily.

%package -n myspell-gl_ES
Summary:	MySpell spelling dictionaries for Galician (Spain)
Version:	%{_ver}
Release:	0.20030905.%{_rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	mozilla-thunderbird-dictionary-gl
Provides:	myspell-dictionary = %{version}
Provides:	myspell-gl = %{version}
Obsoletes:	mozilla-thunderbird-dictionary-gl
Obsoletes:	myspell-gl

%description -n myspell-gl_ES
myspell-gl_ES contains spell checking data in Galician (Spain) to be
used by OpenOffice.org or MySpell-capable applications like Mozilla.
With this extension, you can compose a document in Galician and check
for the typos easily.

%package -n myspell-hr_HR
Summary:	MySpell spelling dictionaries for Croatian (Croatia)
Version:	%{_ver}
Release:	0.20020411.%{_rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	mozilla-thunderbird-dictionary-hr
Provides:	myspell-dictionary = %{version}
Provides:	myspell-hr = %{version}
Obsoletes:	mozilla-thunderbird-dictionary-hr
Obsoletes:	myspell-hr

%description -n myspell-hr_HR
myspell-hr_HR contains spell checking data in Croatian (Croatia) to be
used by OpenOffice.org or MySpell-capable applications like Mozilla.
With this extension, you can compose a document in Croatian and check
for the typos easily.

%package -n myspell-hu_HU
Summary:	MySpell spelling dictionaries for Hungarian (Hungary)
Version:	%{_ver}
Release:	0.20040331.%{_rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	mozilla-thunderbird-dictionary-hu
Provides:	myspell-dictionary = %{version}
Provides:	myspell-hu = %{version}
Obsoletes:	mozilla-thunderbird-dictionary-hu
Obsoletes:	myspell-hu

%description -n myspell-hu_HU
myspell-hu_HU contains spell checking data in Hungarian (Hungary) to
be used by OpenOffice.org or MySpell-capable applications like
Mozilla. With this extension, you can compose a document in Hungarian
and check for the typos easily.

%package -n myspell-id_ID
Summary:	MySpell spelling dictionaries for Indonesian (Indonesia)
Version:	%{_ver}
Release:	0.20040810.%{_rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	myspell-dictionary = %{version}
Provides:	myspell-id = %{version}
Obsoletes:	myspell-id

%description -n myspell-id_ID
myspell-id_ID contains spell checking data in Indonesian (Indonesia)
to be used by OpenOffice.org or MySpell-capable applications like
Mozilla. With this extension, you can compose a document in Indonesian
and check for the typos easily.

%package -n myspell-it_IT
Summary:	MySpell spelling dictionaries for Italian (Italy)
Version:	%{_ver}
Release:	0.20040624.%{_rel}
License:	LGPL/GPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	mozilla-thunderbird-dictionary-it
Provides:	myspell-dictionary = %{version}
Provides:	myspell-it = %{version}
Obsoletes:	mozilla-thunderbird-dictionary-it
Obsoletes:	myspell-it

%description -n myspell-it_IT
myspell-it_IT contains spell checking data in Italian (Italy) to be
used by OpenOffice.org or MySpell-capable applications like Mozilla.
With this extension, you can compose a document in Italian and check
for the typos easily.

%package -n myspell-lt_LT
Summary:	MySpell spelling dictionaries for Lithuanian (Lithuania)
Version:	%{_ver}
Release:	0.20031231.%{_rel}
License:	BSD-like
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	mozilla-thunderbird-dictionary-lt
Provides:	myspell-dictionary = %{version}
Provides:	myspell-lt = %{version}
Obsoletes:	mozilla-thunderbird-dictionary-lt
Obsoletes:	myspell-lt

%description -n myspell-lt_LT
myspell-lt_LT contains spell checking data in Lithuanian (Lithuania)
to be used by OpenOffice.org or MySpell-capable applications like
Mozilla. With this extension, you can compose a document in Lithuanian
and check for the typos easily.

%package -n myspell-mi_NZ
Summary:	MySpell spelling dictionaries for Maori (New Zealand)
Version:	%{_ver}
Release:	0.20030909.%{_rel}
License:	LGPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	mozilla-thunderbird-dictionary-mi
Provides:	myspell-dictionary = %{version}
Provides:	myspell-mi = %{version}
Obsoletes:	mozilla-thunderbird-dictionary-mi
Obsoletes:	myspell-mi

%description -n myspell-mi_NZ
myspell-mi_NZ contains spell checking data in Maori (New Zealand) to
be used by OpenOffice.org or MySpell-capable applications like
Mozilla. With this extension, you can compose a document in Maori and
check for the typos easily.

%package -n myspell-ms_MY
Summary:	MySpell spelling dictionaries for Malay (Malaysia)
Version:	%{_ver}
Release:	0.20040907.%{_rel}
License:	GNU Free Documentation License
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	mozilla-thunderbird-dictionary-ms
Provides:	myspell-dictionary = %{version}
Provides:	myspell-ms = %{version}
Obsoletes:	mozilla-thunderbird-dictionary-ms
Obsoletes:	myspell-ms

%description -n myspell-ms_MY
myspell-ms_MY contains spell checking data in Malay (Malaysia) to be
used by OpenOffice.org or MySpell-capable applications like Mozilla.
With this extension, you can compose a document in Malay and check for
the typos easily.

%package -n myspell-nb_NO
Summary:	MySpell spelling dictionaries for Norwegian/Bokm¿l (Norway)
Version:	%{_ver}
Release:	0.20031013.%{_rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	mozilla-thunderbird-dictionary-nb
Provides:	myspell-dictionary = %{version}
Provides:	myspell-no = %{version}
Obsoletes:	mozilla-thunderbird-dictionary-nb
Obsoletes:	myspell-no

%description -n myspell-nb_NO
myspell-nb_NO contains spell checking data in Norwegian/Bokm

%package -n myspell-nl_NL
Summary:	MySpell spelling dictionaries for Dutch (Netherland)
Version:	%{_ver}
Release:	0.20040222.%{_rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	mozilla-thunderbird-dictionary-nl
Provides:	myspell-dictionary = %{version}
Provides:	myspell-nl = %{version}
Obsoletes:	mozilla-thunderbird-dictionary-nl
Obsoletes:	myspell-nl

%description -n myspell-nl_NL
myspell-nl_NL contains spell checking data in Dutch (Netherland) to be
used by OpenOffice.org or MySpell-capable applications like Mozilla.
With this extension, you can compose a document in Dutch and check for
the typos easily.

%package -n myspell-nn_NO
Summary:	MySpell spelling dictionaries for Norwegian/Nynorsk (Norway)
Version:	%{_ver}
Release:	0.20031013.%{_rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	mozilla-thunderbird-dictionary-nn
Provides:	myspell-dictionary = %{version}
Provides:	myspell-no = %{version}
Obsoletes:	mozilla-thunderbird-dictionary-nn
Obsoletes:	myspell-no

%description -n myspell-nn_NO
myspell-nn_NO contains spell checking data in Norwegian/Nynorsk
(Norway) to be used by OpenOffice.org or MySpell-capable applications
like Mozilla. With this extension, you can compose a document in
Norwegian/Nynorsk and check for the typos easily.

%package -n myspell-pl_PL
Summary:	MySpell spelling dictionaries for Polish (Poland)
Version:	%{_ver}
Release:	0.20040816.%{_rel}
License:	Creative Commons ShareAlike, http://creativecommons.org/licenses/sa/1.0
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	mozilla-thunderbird-dictionary-pl
Provides:	myspell-dictionary = %{version}
Provides:	myspell-pl = %{version}
Obsoletes:	mozilla-thunderbird-dictionary-pl
Obsoletes:	myspell-pl

%description -n myspell-pl_PL
myspell-pl_PL contains spell checking data in Polish (Poland) to be
used by OpenOffice.org or MySpell-capable applications like Mozilla.
With this extension, you can compose a document in Polish and check
for the typos easily.

%package -n myspell-pt_BR
Summary:	MySpell spelling dictionaries for Portuguese (Brasil)
Version:	%{_ver}
Release:	0.20030110.%{_rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	mozilla-thunderbird-dictionary-pt-BR
Provides:	myspell-dictionary = %{version}
Obsoletes:	mozilla-thunderbird-dictionary-pt-BR

%description -n myspell-pt_BR
myspell-pt_BR contains spell checking data in Portuguese (Brasil) to
be used by OpenOffice.org or MySpell-capable applications like
Mozilla. With this extension, you can compose a document in Portuguese
and check for the typos easily.

%package -n myspell-pt_PT
Summary:	MySpell spelling dictionaries for Portuguese (Portugal)
Version:	%{_ver}
Release:	0.20020629.%{_rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	mozilla-thunderbird-dictionary-pt
Provides:	myspell-dictionary = %{version}
Provides:	myspell-pt = %{version}
Obsoletes:	mozilla-thunderbird-dictionary-pt
Obsoletes:	myspell-pt

%description -n myspell-pt_PT
myspell-pt_PT contains spell checking data in Portuguese (Portugal) to
be used by OpenOffice.org or MySpell-capable applications like
Mozilla. With this extension, you can compose a document in Portuguese
and check for the typos easily.

%package -n myspell-ro_RO
Summary:	MySpell spelling dictionaries for Romanian (Romania)
Version:	%{_ver}
Release:	0.20031023.%{_rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	mozilla-thunderbird-dictionary-ro
Provides:	myspell-dictionary = %{version}
Provides:	myspell-ro = %{version}
Obsoletes:	mozilla-thunderbird-dictionary-ro
Obsoletes:	myspell-ro

%description -n myspell-ro_RO
myspell-ro_RO contains spell checking data in Romanian (Romania) to be
used by OpenOffice.org or MySpell-capable applications like Mozilla.
With this extension, you can compose a document in Romanian and check
for the typos easily.

%package -n myspell-ru_RU
Summary:	MySpell spelling dictionaries for Russian (Russia)
Version:	%{_ver}
Release:	0.20040406.%{_rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	mozilla-thunderbird-dictionary-ru
Provides:	myspell-dictionary = %{version}
Provides:	myspell-ru = %{version}
Obsoletes:	mozilla-thunderbird-dictionary-ru
Obsoletes:	myspell-ru

%description -n myspell-ru_RU
myspell-ru_RU contains spell checking data in Russian (Russia) to be
used by OpenOffice.org or MySpell-capable applications like Mozilla.
With this extension, you can compose a document in Russian and check
for the typos easily.

%package -n myspell-sk_SK
Summary:	MySpell spelling dictionaries for Slovak (Slovak Republic)
Version:	%{_ver}
Release:	0.20040118.%{_rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	mozilla-thunderbird-dictionary-sk
Provides:	myspell-dictionary = %{version}
Provides:	myspell-sk = %{version}
Obsoletes:	mozilla-thunderbird-dictionary-sk
Obsoletes:	myspell-sk

%description -n myspell-sk_SK
myspell-sk_SK contains spell checking data in Slovak (Slovak Republic)
to be used by OpenOffice.org or MySpell-capable applications like
Mozilla. With this extension, you can compose a document in Slovak and
check for the typos easily.

%package -n myspell-sl_SI
Summary:	MySpell spelling dictionaries for Slovenian (Slovenia)
Version:	%{_ver}
Release:	0.20030907.%{_rel}
License:	BSD-like
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	mozilla-thunderbird-dictionary-sl
Provides:	myspell-dictionary = %{version}
Provides:	myspell-sl = %{version}
Obsoletes:	mozilla-thunderbird-dictionary-sl
Obsoletes:	myspell-sl

%description -n myspell-sl_SI
myspell-sl_SI contains spell checking data in Slovenian (Slovenia) to
be used by OpenOffice.org or MySpell-capable applications like
Mozilla. With this extension, you can compose a document in Slovenian
and check for the typos easily.

%package -n myspell-sv_SE
Summary:	MySpell spelling dictionaries for Swedish (Sweden)
Version:	%{_ver}
Release:	0.20030814.%{_rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	mozilla-thunderbird-dictionary-sv
Provides:	myspell-dictionary = %{version}
Provides:	myspell-sv = %{version}
Obsoletes:	mozilla-thunderbird-dictionary-sv
Obsoletes:	myspell-sv

%description -n myspell-sv_SE
myspell-sv_SE contains spell checking data in Swedish (Sweden) to be
used by OpenOffice.org or MySpell-capable applications like Mozilla.
With this extension, you can compose a document in Swedish and check
for the typos easily.

%package -n myspell-sw_KE
Summary:	MySpell spelling dictionaries for Kiswahili (Africa)
Version:	%{_ver}
Release:	0.20040516.%{_rel}
License:	LGPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	myspell-dictionary = %{version}
Provides:	myspell-sw = %{version}
Obsoletes:	myspell-sw

%description -n myspell-sw_KE
myspell-sw_KE contains spell checking data in Kiswahili (Africa) to be
used by OpenOffice.org or MySpell-capable applications like Mozilla.
With this extension, you can compose a document in Kiswahili and check
for the typos easily.

%package -n myspell-uk_UA
Summary:	MySpell spelling dictionaries for Ukrainian (Ukraine)
Version:	%{_ver}
Release:	0.20031016.%{_rel}
License:	LGPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	mozilla-thunderbird-dictionary-uk
Provides:	myspell-dictionary = %{version}
Provides:	myspell-uk = %{version}
Obsoletes:	mozilla-thunderbird-dictionary-uk
Obsoletes:	myspell-uk

%description -n myspell-uk_UA
myspell-uk_UA contains spell checking data in Ukrainian (Ukraine) to
be used by OpenOffice.org or MySpell-capable applications like
Mozilla. With this extension, you can compose a document in Ukrainian
and check for the typos easily.

%package -n myspell-zu_ZA
Summary:	MySpell spelling dictionaries for Zulu (South Africa)
Version:	%{_ver}
Release:	0.20040604.%{_rel}
License:	LGPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	mozilla-thunderbird-dictionary-zu-ZA
Provides:	myspell-dictionary = %{version}
Provides:	myspell-zu = %{version}
Obsoletes:	mozilla-thunderbird-dictionary-zu-ZA
Obsoletes:	myspell-zu

%description -n myspell-zu_ZA
myspell-zu_ZA contains spell checking data in Zulu (South Africa) to
be used by OpenOffice.org or MySpell-capable applications like
Mozilla. With this extension, you can compose a document in Zulu and
check for the typos easily.

# Hyphenation
%package -n myspell-hyph-bg
Summary:	MySpell hyphenation dictionaries for Bulgarian
Version:	%{_ver}
Release:	0.20040417.%{_rel}
License:	LGPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	myspell-hyphenation = %{version}

%description -n myspell-hyph-bg
myspell-hyph-bg contains hyphenation data for Bulgarian to be used by
OpenOffice.org or MySpell-capable applications like Mozilla.

%package -n myspell-hyph-cs
Summary:	MySpell hyphenation dictionaries for Czech
Version:	%{_ver}
Release:	0.20030101.%{_rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	myspell-hyphenation = %{version}

%description -n myspell-hyph-cs
myspell-hyph-cs contains hyphenation data for Czech to be used by
OpenOffice.org or MySpell-capable applications like Mozilla.

%package -n myspell-hyph-da
Summary:	MySpell hyphenation dictionaries for Danish
Version:	%{_ver}
Release:	0.20020727.%{_rel}
License:	LGPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	myspell-hyphenation = %{version}

%description -n myspell-hyph-da
myspell-hyph-da contains hyphenation data for Danish to be used by
OpenOffice.org or MySpell-capable applications like Mozilla.

%package -n myspell-hyph-de
Summary:	MySpell hyphenation dictionaries for German
Version:	%{_ver}
Release:	0.20020727.%{_rel}
License:	LGPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	myspell-hyphenation = %{version}

%description -n myspell-hyph-de
myspell-hyph-de contains hyphenation data for German to be used by
OpenOffice.org or MySpell-capable applications like Mozilla.

%package -n myspell-hyph-el
Summary:	MySpell hyphenation dictionaries for Greek
Version:	%{_ver}
Release:	0.20040409.%{_rel}
License:	LGPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	myspell-hyphenation = %{version}

%description -n myspell-hyph-el
myspell-hyph-el contains hyphenation data for Greek to be used by
OpenOffice.org or MySpell-capable applications like Mozilla.

%package -n myspell-hyph-en
Summary:	MySpell hyphenation dictionaries for English
Version:	%{_ver}
Release:	0.20020727.%{_rel}
License:	LGPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	myspell-hyphenation = %{version}

%description -n myspell-hyph-en
myspell-hyph-en contains hyphenation data for English to be used by
OpenOffice.org or MySpell-capable applications like Mozilla.

%package -n myspell-hyph-es
Summary:	MySpell hyphenation dictionaries for Spanish
Version:	%{_ver}
Release:	0.20040602.%{_rel}
License:	LGPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	myspell-hyphenation = %{version}

%description -n myspell-hyph-es
myspell-hyph-es contains hyphenation data for Spanish to be used by
OpenOffice.org or MySpell-capable applications like Mozilla.

%package -n myspell-hyph-et
Summary:	MySpell hyphenation dictionaries for Estonian
Version:	%{_ver}
Release:	0.20040621.%{_rel}
License:	free, see http://www.eki.ee/eki/licence.html
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	myspell-hyphenation = %{version}

%description -n myspell-hyph-et
myspell-hyph-et contains hyphenation data for Estonian to be used by
OpenOffice.org or MySpell-capable applications like Mozilla.

%package -n myspell-hyph-fi
Summary:	MySpell hyphenation dictionaries for Finnish
Version:	%{_ver}
Release:	0.20031125.%{_rel}
License:	freely distributable
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	myspell-hyphenation = %{version}

%description -n myspell-hyph-fi
myspell-hyph-fi contains hyphenation data for Finnish to be used by
OpenOffice.org or MySpell-capable applications like Mozilla.

%package -n myspell-hyph-fr
Summary:	MySpell hyphenation dictionaries for French
Version:	%{_ver}
Release:	0.20020727.%{_rel}
License:	LGPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	myspell-hyphenation = %{version}

%description -n myspell-hyph-fr
myspell-hyph-fr contains hyphenation data for French to be used by
OpenOffice.org or MySpell-capable applications like Mozilla.

%package -n myspell-hyph-ga
Summary:	MySpell hyphenation dictionaries for Irish
Version:	%{_ver}
Release:	0.20040212.%{_rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	myspell-hyphenation = %{version}

%description -n myspell-hyph-ga
myspell-hyph-ga contains hyphenation data for Irish to be used by
OpenOffice.org or MySpell-capable applications like Mozilla.

%package -n myspell-hyph-hu
Summary:	MySpell hyphenation dictionaries for Hungarian
Version:	%{_ver}
Release:	0.20031107.%{_rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	myspell-hyphenation = %{version}

%description -n myspell-hyph-hu
myspell-hyph-hu contains hyphenation data for Hungarian to be used by
OpenOffice.org or MySpell-capable applications like Mozilla.

%package -n myspell-hyph-id
Summary:	MySpell hyphenation dictionaries for Indonesian
Version:	%{_ver}
Release:	0.20040810.%{_rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	myspell-hyphenation = %{version}

%description -n myspell-hyph-id
myspell-hyph-id contains hyphenation data for Indonesian to be used by
OpenOffice.org or MySpell-capable applications like Mozilla.

%package -n myspell-hyph-is
Summary:	MySpell hyphenation dictionaries for Icelandic
Version:	%{_ver}
Release:	0.20030918.%{_rel}
License:	LGPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	myspell-hyphenation = %{version}

%description -n myspell-hyph-is
myspell-hyph-is contains hyphenation data for Icelandic to be used by
OpenOffice.org or MySpell-capable applications like Mozilla.

%package -n myspell-hyph-it
Summary:	MySpell hyphenation dictionaries for Italian
Version:	%{_ver}
Release:	0.20030904.%{_rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	myspell-hyphenation = %{version}

%description -n myspell-hyph-it
myspell-hyph-it contains hyphenation data for Italian to be used by
OpenOffice.org or MySpell-capable applications like Mozilla.

%package -n myspell-hyph-lt
Summary:	MySpell hyphenation dictionaries for Lithuanian
Version:	%{_ver}
Release:	0.20040111.%{_rel}
License:	LPPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	myspell-hyphenation = %{version}

%description -n myspell-hyph-lt
myspell-hyph-lt contains hyphenation data for Lithuanian to be used by
OpenOffice.org or MySpell-capable applications like Mozilla.

%package -n myspell-hyph-nl
Summary:	MySpell hyphenation dictionaries for Dutch
Version:	%{_ver}
Release:	0.20040222.%{_rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	myspell-hyphenation = %{version}

%description -n myspell-hyph-nl
myspell-hyph-nl contains hyphenation data for Dutch to be used by
OpenOffice.org or MySpell-capable applications like Mozilla.

%package -n myspell-hyph-pl
Summary:	MySpell hyphenation dictionaries for Polish
Version:	%{_ver}
Release:	0.20030913.%{_rel}
License:	LGPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	myspell-hyphenation = %{version}

%description -n myspell-hyph-pl
myspell-hyph-pl contains hyphenation data for Polish to be used by
OpenOffice.org or MySpell-capable applications like Mozilla.

%package -n myspell-hyph-pt
Summary:	MySpell hyphenation dictionaries for Portuguese
Version:	%{_ver}
Release:	0.20030904.%{_rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	myspell-hyphenation = %{version}

%description -n myspell-hyph-pt
myspell-hyph-pt contains hyphenation data for Portuguese to be used by
OpenOffice.org or MySpell-capable applications like Mozilla.

%package -n myspell-hyph-ru
Summary:	MySpell hyphenation dictionaries for Russian
Version:	%{_ver}
Release:	0.20020727.%{_rel}
License:	LGPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	myspell-hyphenation = %{version}

%description -n myspell-hyph-ru
myspell-hyph-ru contains hyphenation data for Russian to be used by
OpenOffice.org or MySpell-capable applications like Mozilla.

%package -n myspell-hyph-sk
Summary:	MySpell hyphenation dictionaries for Slovak
Version:	%{_ver}
Release:	0.20030101.%{_rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	myspell-hyphenation = %{version}

%description -n myspell-hyph-sk
myspell-hyph-sk contains hyphenation data for Slovak to be used by
OpenOffice.org or MySpell-capable applications like Mozilla.

%package -n myspell-hyph-sl
Summary:	MySpell hyphenation dictionaries for Slovenian
Version:	%{_ver}
Release:	0.20021003.%{_rel}
License:	Copyright Matjaz Vrecko
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	myspell-hyphenation = %{version}

%description -n myspell-hyph-sl
myspell-hyph-sl contains hyphenation data for Slovenian to be used by
OpenOffice.org or MySpell-capable applications like Mozilla.

%package -n myspell-hyph-sv
Summary:	MySpell hyphenation dictionaries for Swedish
Version:	%{_ver}
Release:	0.20030814.%{_rel}
License:	LGPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	myspell-hyphenation = %{version}

%description -n myspell-hyph-sv
myspell-hyph-sv contains hyphenation data for Swedish to be used by
OpenOffice.org or MySpell-capable applications like Mozilla.

%package -n myspell-hyph-uk
Summary:	MySpell hyphenation dictionaries for Ukrainian
Version:	%{_ver}
Release:	0.20021219.%{_rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	myspell-hyphenation = %{version}

%description -n myspell-hyph-uk
myspell-hyph-uk contains hyphenation data for Ukrainian to be used by
OpenOffice.org or MySpell-capable applications like Mozilla.

# Thesaurus
%package -n myspell-thes-bg_BG
Summary:	MySpell thesaurus for Bulgarian (Bulgaria)
Version:	%{_ver}
Release:	0.20040402.%{_rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	myspell-thesaurus = %{version}

%description -n myspell-thes-bg_BG
myspell-thes-bg_BG contains thesaurus data in Bulgarian (Bulgaria) to
be used by MySpell-capable applications like OpenOffice.org.

%package -n myspell-thes-de_DE
Summary:	MySpell thesaurus for German (Germany)
Version:	%{_ver}
Release:	0.20040702.%{_rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	myspell-thesaurus = %{version}

%description -n myspell-thes-de_DE
myspell-thes-de_DE contains thesaurus data in German (Germany) to be
used by MySpell-capable applications like OpenOffice.org.

%package -n myspell-thes-en_US
Summary:	MySpell thesaurus for English (US)
Version:	%{_ver}
Release:	0.20040423.%{_rel}
License:	BSD
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	myspell-thesaurus = %{version}

%description -n myspell-thes-en_US
myspell-thes-en_US contains thesaurus data in English (US) to be used
by MySpell-capable applications like OpenOffice.org.

%package -n myspell-thes-es_ES
Summary:	MySpell thesaurus for Spanish (Spain)
Version:	%{_ver}
Release:	0.20040712.%{_rel}
License:	LGPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	myspell-thesaurus = %{version}

%description -n myspell-thes-es_ES
myspell-thes-es_ES contains thesaurus data in Spanish (Spain) to be
used by MySpell-capable applications like OpenOffice.org.

%package -n myspell-thes-fr_FR
Summary:	MySpell thesaurus for French (France)
Version:	%{_ver}
Release:	0.20030819.%{_rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	myspell-thesaurus = %{version}

%description -n myspell-thes-fr_FR
myspell-thes-fr_FR contains thesaurus data in French (France) to be
used by MySpell-capable applications like OpenOffice.org.

%package -n myspell-thes-it_IT
Summary:	MySpell thesaurus for Italian (Italy)
Version:	%{_ver}
Release:	0.20040222.%{_rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	myspell-thesaurus = %{version}

%description -n myspell-thes-it_IT
myspell-thes-it_IT contains thesaurus data in Italian (Italy) to be
used by MySpell-capable applications like OpenOffice.org.

%package -n myspell-thes-pl_PL
Summary:	MySpell thesaurus for Polish (Poland)
Version:	%{_ver}
Release:	0.20040803.%{_rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	myspell-thesaurus = %{version}

%description -n myspell-thes-pl_PL
myspell-thes-pl_PL contains thesaurus data in Polish (Poland) to be
used by MySpell-capable applications like OpenOffice.org.

%package -n myspell-thes-sk_SK
Summary:	MySpell thesaurus for Slovak (Slovak Republic)
Version:	%{_ver}
Release:	0.20050218.%{_rel}
License:	GPL
Group:		Applications/Text
Requires:	myspell-common = %{_ver}-%{_rel}
Provides:	myspell-thesaurus = %{version}

%description -n myspell-thes-sk_SK
myspell-thes-sk_SK contains thesaurus data in Slovak (Slovak Republic)
to be used by MySpell-capable applications like OpenOffice.org.

%prep
%setup -q -c -T

# Handle spelling dictionaries
for dictfile in %{SOURCE100} %{SOURCE101} %{SOURCE102} %{SOURCE103} %{SOURCE104} \
		%{SOURCE105} %{SOURCE106} %{SOURCE107} %{SOURCE108} %{SOURCE109} \
		%{SOURCE110} %{SOURCE111} %{SOURCE112} %{SOURCE113} %{SOURCE114} \
		%{SOURCE115} %{SOURCE116} %{SOURCE117} %{SOURCE118} %{SOURCE119} \
		%{SOURCE120} %{SOURCE121} %{SOURCE122} %{SOURCE123} %{SOURCE124} \
		%{SOURCE125} %{SOURCE126} %{SOURCE127} %{SOURCE128} %{SOURCE129} \
		%{SOURCE130} %{SOURCE131} %{SOURCE132} %{SOURCE133} %{SOURCE134} \
		%{SOURCE135} %{SOURCE136} %{SOURCE137} %{SOURCE138} %{SOURCE139} \
		%{SOURCE140} %{SOURCE141} %{SOURCE142} %{SOURCE143}; do
	basefile="${dictfile##*/}"
	langpack="${basefile%.zip}"
	echo "LANGPACK=$langpack"
	mkdir -p doc/DICT/$langpack
	%{__unzip} -q -d doc/DICT/$langpack $dictfile
	mkdir -p dic/DICT/$langpack
	mv doc/DICT/$langpack/$langpack.{aff,dic} dic/DICT/$langpack
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
		%{SOURCE220} %{SOURCE221} %{SOURCE222} %{SOURCE223}; do
	basefile="${hyphfile##*/}"
	langpack="${basefile%.zip}"
	echo "LANGPACK/(HPY)=$langpack"
	mkdir -p doc/HYPH/$langpack
	%{__unzip} -q -d doc/HYPH/$langpack $hyphfile
	mkdir -p dic/HYPH/$langpack
	mv doc/HYPH/$langpack/$langpack.dic dic/HYPH/$langpack
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
	basefile="${thesfile##*/}"
	langpack="${basefile%.zip}"
	echo "LANGPACK(thes)=$langpack"
	mkdir -p doc/THES/$langpack
	%{__unzip} -q -d doc/THES/$langpack $thesfile
	mkdir -p dic/THES/$langpack
	mv doc/THES/$langpack/$langpack.{dat,idx} dic/THES/$langpack
	# create dummy file if docdir is empty
	if ! ls doc/THES/$langpack/*; then
		cat > doc/THES/$langpack/README_$langpack.txt << EOF
Thesaurus dictionary for $langpack
EOF
	fi
done

%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{dictdir}

# Install spell checking dictionaries
for file in dic/DICT/*/*; do
	install -m 644 $file $RPM_BUILD_ROOT%{dictdir}/${file##*/}
done

# Install hyphenation dictionaries
for file in dic/HYPH/*/*; do
	install -m 644 $file $RPM_BUILD_ROOT%{dictdir}/${file##*/}
done

# Install thesaurus dictionaries
for file in dic/THES/*/*; do
	install -m 644 $file $RPM_BUILD_ROOT%{dictdir}/${file##*/}
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
	perl -ni -e "/^DICT\s*af\s*ZA\s*af_ZA$/ or print" %{dictdir}/dictionary.lst
fi

%post -n myspell-bg_BG
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*bg[ \t]*BG[ \t]*bg_BG" %{dictdir}/dictionary.lst; then
	echo "DICT bg BG bg_BG" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-bg_BG
if [ "$1" = "0" ]; then
	perl -ni -e "/^DICT\s*bg\s*BG\s*bg_BG$/ or print" %{dictdir}/dictionary.lst
fi

%post -n myspell-ca_ES
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*ca[ \t]*ES[ \t]*ca_ES" %{dictdir}/dictionary.lst; then
	echo "DICT ca ES ca_ES" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-ca_ES
if [ "$1" = "0" ]; then
	perl -ni -e "/^DICT\s*ca\s*ES\s*ca_ES$/ or print" %{dictdir}/dictionary.lst
fi

%post -n myspell-cs_CZ
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*cs[ \t]*CZ[ \t]*cs_CZ" %{dictdir}/dictionary.lst; then
	echo "DICT cs CZ cs_CZ" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-cs_CZ
if [ "$1" = "0" ]; then
	perl -ni -e "/^DICT\s*cs\s*CZ\s*cs_CZ$/ or print" %{dictdir}/dictionary.lst
fi

%post -n myspell-cy_GB
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*cy[ \t]*GB[ \t]*cy_GB" %{dictdir}/dictionary.lst; then
	echo "DICT cy GB cy_GB" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-cy_GB
if [ "$1" = "0" ]; then
	perl -ni -e "/^DICT\s*cy\s*GB\s*cy_GB$/ or print" %{dictdir}/dictionary.lst
fi

%post -n myspell-da_DK
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*da[ \t]*DK[ \t]*da_DK" %{dictdir}/dictionary.lst; then
	echo "DICT da DK da_DK" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-da_DK
if [ "$1" = "0" ]; then
	perl -ni -e "/^DICT\s*da\s*DK\s*da_DK$/ or print" %{dictdir}/dictionary.lst
fi

%post -n myspell-de_AT
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*de[ \t]*AT[ \t]*de_AT" %{dictdir}/dictionary.lst; then
	echo "DICT de AT de_AT" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-de_AT
if [ "$1" = "0" ]; then
	perl -ni -e "/^DICT\s*de\s*AT\s*de_AT$/ or print" %{dictdir}/dictionary.lst
fi

%post -n myspell-el_GR
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*el[ \t]*GR[ \t]*el_GR" %{dictdir}/dictionary.lst; then
	echo "DICT el GR el_GR" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-el_GR
if [ "$1" = "0" ]; then
	perl -ni -e "/^DICT\s*el\s*GR\s*el_GR$/ or print" %{dictdir}/dictionary.lst
fi

%post -n myspell-en_US
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*en[ \t]*US[ \t]*en_US" %{dictdir}/dictionary.lst; then
	echo "DICT en US en_US" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-en_US
if [ "$1" = "0" ]; then
	perl -ni -e "/^DICT\s*en\s*US\s*en_US$/ or print" %{dictdir}/dictionary.lst
fi

%post -n myspell-en_NZ
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*en[ \t]*NZ[ \t]*en_NZ" %{dictdir}/dictionary.lst; then
	echo "DICT en NZ en_NZ" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-en_NZ
if [ "$1" = "0" ]; then
	perl -ni -e "/^DICT\s*en\s*NZ\s*en_NZ$/ or print" %{dictdir}/dictionary.lst
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
	perl -ni -e "/^DICT\s*es\s*MX\s*es_MX$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^DICT\s*es\s*AR\s*es_MX$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^DICT\s*es\s*CO\s*es_MX$/ or print" %{dictdir}/dictionary.lst
fi

%post -n myspell-et_EE
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*et[ \t]*EE[ \t]*et_EE" %{dictdir}/dictionary.lst; then
	echo "DICT et EE et_EE" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-et_EE
if [ "$1" = "0" ]; then
	perl -ni -e "/^DICT\s*et\s*EE\s*et_EE$/ or print" %{dictdir}/dictionary.lst
fi

%post -n myspell-fo_FO
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*fo[ \t]*FO[ \t]*fo_FO" %{dictdir}/dictionary.lst; then
	echo "DICT fo FO fo_FO" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-fo_FO
if [ "$1" = "0" ]; then
	perl -ni -e "/^DICT\s*fo\s*FO\s*fo_FO$/ or print" %{dictdir}/dictionary.lst
fi

%post -n myspell-fr_BE
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*fr[ \t]*BE[ \t]*fr_BE" %{dictdir}/dictionary.lst; then
	echo "DICT fr BE fr_BE" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-fr_BE
if [ "$1" = "0" ]; then
	perl -ni -e "/^DICT\s*fr\s*BE\s*fr_BE$/ or print" %{dictdir}/dictionary.lst
fi

%post -n myspell-ga_IE
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*ga[ \t]*IE[ \t]*ga_IE" %{dictdir}/dictionary.lst; then
	echo "DICT ga IE ga_IE" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-ga_IE
if [ "$1" = "0" ]; then
	perl -ni -e "/^DICT\s*ga\s*IE\s*ga_IE$/ or print" %{dictdir}/dictionary.lst
fi

%post -n myspell-gl_ES
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*gl[ \t]*ES[ \t]*gl_ES" %{dictdir}/dictionary.lst; then
	echo "DICT gl ES gl_ES" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-gl_ES
if [ "$1" = "0" ]; then
	perl -ni -e "/^DICT\s*gl\s*ES\s*gl_ES$/ or print" %{dictdir}/dictionary.lst
fi

%post -n myspell-hr_HR
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*hr[ \t]*HR[ \t]*hr_HR" %{dictdir}/dictionary.lst; then
	echo "DICT hr HR hr_HR" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-hr_HR
if [ "$1" = "0" ]; then
	perl -ni -e "/^DICT\s*hr\s*HR\s*hr_HR$/ or print" %{dictdir}/dictionary.lst
fi

%post -n myspell-hu_HU
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*hu[ \t]*HU[ \t]*hu_HU" %{dictdir}/dictionary.lst; then
	echo "DICT hu HU hu_HU" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-hu_HU
if [ "$1" = "0" ]; then
	perl -ni -e "/^DICT\s*hu\s*HU\s*hu_HU$/ or print" %{dictdir}/dictionary.lst
fi

%post -n myspell-id_ID
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*id[ \t]*ID[ \t]*id_ID" %{dictdir}/dictionary.lst; then
	echo "DICT id ID id_ID" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-id_ID
if [ "$1" = "0" ]; then
	perl -ni -e "/^DICT\s*id\s*ID\s*id_ID$/ or print" %{dictdir}/dictionary.lst
fi

%post -n myspell-it_IT
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*it[ \t]*IT[ \t]*it_IT" %{dictdir}/dictionary.lst; then
	echo "DICT it IT it_IT" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-it_IT
if [ "$1" = "0" ]; then
	perl -ni -e "/^DICT\s*it\s*IT\s*it_IT$/ or print" %{dictdir}/dictionary.lst
fi

%post -n myspell-lt_LT
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*lt[ \t]*LT[ \t]*lt_LT" %{dictdir}/dictionary.lst; then
	echo "DICT lt LT lt_LT" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-lt_LT
if [ "$1" = "0" ]; then
	perl -ni -e "/^DICT\s*lt\s*LT\s*lt_LT$/ or print" %{dictdir}/dictionary.lst
fi

%post -n myspell-mi_NZ
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*mi[ \t]*NZ[ \t]*mi_NZ" %{dictdir}/dictionary.lst; then
	echo "DICT mi NZ mi_NZ" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-mi_NZ
if [ "$1" = "0" ]; then
	perl -ni -e "/^DICT\s*mi\s*NZ\s*mi_NZ$/ or print" %{dictdir}/dictionary.lst
fi

%post -n myspell-ms_MY
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*ms[ \t]*MY[ \t]*ms_MY" %{dictdir}/dictionary.lst; then
	echo "DICT ms MY ms_MY" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-ms_MY
if [ "$1" = "0" ]; then
	perl -ni -e "/^DICT\s*ms\s*MY\s*ms_MY$/ or print" %{dictdir}/dictionary.lst
fi

%post -n myspell-nb_NO
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*nb[ \t]*NO[ \t]*nb_NO" %{dictdir}/dictionary.lst; then
	echo "DICT nb NO nb_NO" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-nb_NO
if [ "$1" = "0" ]; then
	perl -ni -e "/^DICT\s*nb\s*NO\s*nb_NO$/ or print" %{dictdir}/dictionary.lst
fi

%post -n myspell-nl_NL
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*nl[ \t]*NL[ \t]*nl_NL" %{dictdir}/dictionary.lst; then
	echo "DICT nl NL nl_NL" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-nl_NL
if [ "$1" = "0" ]; then
	perl -ni -e "/^DICT\s*nl\s*NL\s*nl_NL$/ or print" %{dictdir}/dictionary.lst
fi

%post -n myspell-nn_NO
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*nn[ \t]*NO[ \t]*nn_NO" %{dictdir}/dictionary.lst; then
	echo "DICT nn NO nn_NO" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-nn_NO
if [ "$1" = "0" ]; then
	perl -ni -e "/^DICT\s*nn\s*NO\s*nn_NO$/ or print" %{dictdir}/dictionary.lst
fi

%post -n myspell-pl_PL
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*pl[ \t]*PL[ \t]*pl_PL" %{dictdir}/dictionary.lst; then
	echo "DICT pl PL pl_PL" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-pl_PL
if [ "$1" = "0" ]; then
	perl -ni -e "/^DICT\s*pl\s*PL\s*pl_PL$/ or print" %{dictdir}/dictionary.lst
fi

%post -n myspell-pt_BR
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*pt[ \t]*BR[ \t]*pt_BR" %{dictdir}/dictionary.lst; then
	echo "DICT pt BR pt_BR" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-pt_BR
if [ "$1" = "0" ]; then
	perl -ni -e "/^DICT\s*pt\s*BR\s*pt_BR$/ or print" %{dictdir}/dictionary.lst
fi

%post -n myspell-ro_RO
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*ro[ \t]*RO[ \t]*ro_RO" %{dictdir}/dictionary.lst; then
	echo "DICT ro RO ro_RO" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-ro_RO
if [ "$1" = "0" ]; then
	perl -ni -e "/^DICT\s*ro\s*RO\s*ro_RO$/ or print" %{dictdir}/dictionary.lst
fi

%post -n myspell-ru_RU
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*ru[ \t]*RU[ \t]*ru_RU" %{dictdir}/dictionary.lst; then
	echo "DICT ru RU ru_RU" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-ru_RU
if [ "$1" = "0" ]; then
	perl -ni -e "/^DICT\s*ru\s*RU\s*ru_RU$/ or print" %{dictdir}/dictionary.lst
fi

%post -n myspell-sk_SK
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*sk[ \t]*SK[ \t]*sk_SK" %{dictdir}/dictionary.lst; then
	echo "DICT sk SK sk_SK" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-sk_SK
if [ "$1" = "0" ]; then
	perl -ni -e "/^DICT\s*sk\s*SK\s*sk_SK$/ or print" %{dictdir}/dictionary.lst
fi

%post -n myspell-sl_SI
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*sl[ \t]*SI[ \t]*sl_SI" %{dictdir}/dictionary.lst; then
	echo "DICT sl SI sl_SI" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-sl_SI
if [ "$1" = "0" ]; then
	perl -ni -e "/^DICT\s*sl\s*SI\s*sl_SI$/ or print" %{dictdir}/dictionary.lst
fi

%post -n myspell-sv_SE
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*sv[ \t]*SE[ \t]*sv_SE" %{dictdir}/dictionary.lst; then
	echo "DICT sv SE sv_SE" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-sv_SE
if [ "$1" = "0" ]; then
	perl -ni -e "/^DICT\s*sv\s*SE\s*sv_SE$/ or print" %{dictdir}/dictionary.lst
fi

%post -n myspell-sw_KE
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*sw[ \t]*KE[ \t]*sw_KE" %{dictdir}/dictionary.lst; then
	echo "DICT sw KE sw_KE" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-sw_KE
if [ "$1" = "0" ]; then
	perl -ni -e "/^DICT\s*sw\s*KE\s*sw_KE$/ or print" %{dictdir}/dictionary.lst
fi

%post -n myspell-uk_UA
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*uk[ \t]*UA[ \t]*uk_UA" %{dictdir}/dictionary.lst; then
	echo "DICT uk UA uk_UA" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-uk_UA
if [ "$1" = "0" ]; then
	perl -ni -e "/^DICT\s*uk\s*UA\s*uk_UA$/ or print" %{dictdir}/dictionary.lst
fi

%post -n myspell-zu_ZA
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^DICT[ \t]*zu[ \t]*ZA[ \t]*zu_ZA" %{dictdir}/dictionary.lst; then
	echo "DICT zu ZA zu_ZA" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-zu_ZA
if [ "$1" = "0" ]; then
	perl -ni -e "/^DICT\s*zu\s*ZA\s*zu_ZA$/ or print" %{dictdir}/dictionary.lst
fi

##
## Scripts for hyphenation
##
%post -n myspell-hyph-bg
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*bg[ \t]*BG[ \t]*hyph_bg" %{dictdir}/dictionary.lst; then
	echo "HYPH bg BG hyph_bg" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-hyph-bg
if [ "$1" = "0" ]; then
	perl -ni -e "/^HYPH\s*bg\s*BG\s*hyph_bg$/ or print" %{dictdir}/dictionary.lst
fi

%post -n myspell-hyph-cs
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*cs[ \t]*CZ[ \t]*hyph_cs" %{dictdir}/dictionary.lst; then
	echo "HYPH cs CZ hyph_cs" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-hyph-cs
if [ "$1" = "0" ]; then
	perl -ni -e "/^HYPH\s*cs\s*CZ\s*hyph_cs$/ or print" %{dictdir}/dictionary.lst
fi

%post -n myspell-hyph-da
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*da[ \t]*DA[ \t]*hyph_da" %{dictdir}/dictionary.lst; then
	echo "HYPH da DA hyph_da" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-hyph-da
if [ "$1" = "0" ]; then
	perl -ni -e "/^HYPH\s*da\s*DA\s*hyph_da$/ or print" %{dictdir}/dictionary.lst
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
	perl -ni -e "/^HYPH\s*de\s*DE\s*hyph_de$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^HYPH\s*de\s*AT\s*hyph_de$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^HYPH\s*de\s*CH\s*hyph_de$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^HYPH\s*de\s*LI\s*hyph_de$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^HYPH\s*de\s*LU\s*hyph_de$/ or print" %{dictdir}/dictionary.lst
fi

%post -n myspell-hyph-el
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*el[ \t]*GR[ \t]*hyph_el" %{dictdir}/dictionary.lst; then
	echo "HYPH el GR hyph_el" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-hyph-el
if [ "$1" = "0" ]; then
	perl -ni -e "/^HYPH\s*el\s*GR\s*hyph_el$/ or print" %{dictdir}/dictionary.lst
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
	perl -ni -e "/^HYPH\s*en\s*US\s*hyph_en$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^HYPH\s*en\s*CA\s*hyph_en$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^HYPH\s*en\s*GB\s*hyph_en$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^HYPH\s*en\s*NZ\s*hyph_en$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^HYPH\s*en\s*AU\s*hyph_en$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^HYPH\s*en\s*ZA\s*hyph_en$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^HYPH\s*en\s*IE\s*hyph_en$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^HYPH\s*en\s*JM\s*hyph_en$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^HYPH\s*en\s*PH\s*hyph_en$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^HYPH\s*en\s*TT\s*hyph_en$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^HYPH\s*en\s*ZW\s*hyph_en$/ or print" %{dictdir}/dictionary.lst
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
	perl -ni -e "/^HYPH\s*es\s*ES\s*hyph_es$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^HYPH\s*es\s*AR\s*hyph_es$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^HYPH\s*es\s*BZ\s*hyph_es$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^HYPH\s*es\s*BO\s*hyph_es$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^HYPH\s*es\s*CL\s*hyph_es$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^HYPH\s*es\s*CO\s*hyph_es$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^HYPH\s*es\s*CR\s*hyph_es$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^HYPH\s*es\s*CU\s*hyph_es$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^HYPH\s*es\s*DO\s*hyph_es$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^HYPH\s*es\s*EC\s*hyph_es$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^HYPH\s*es\s*SV\s*hyph_es$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^HYPH\s*es\s*GU\s*hyph_es$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^HYPH\s*es\s*JN\s*hyph_es$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^HYPH\s*es\s*MX\s*hyph_es$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^HYPH\s*es\s*NI\s*hyph_es$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^HYPH\s*es\s*PA\s*hyph_es$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^HYPH\s*es\s*PU\s*hyph_es$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^HYPH\s*es\s*PE\s*hyph_es$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^HYPH\s*es\s*PR\s*hyph_es$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^HYPH\s*es\s*UY\s*hyph_es$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^HYPH\s*es\s*VE\s*hyph_es$/ or print" %{dictdir}/dictionary.lst
fi

%post -n myspell-hyph-et
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*et[ \t]*EE[ \t]*hyph_et" %{dictdir}/dictionary.lst; then
	echo "HYPH et EE hyph_et" >> %{dictdir}/dictionary.lst
fi
%preun -n myspell-hyph-et
if [ "$1" = "0" ]; then
	perl -ni -e "/^HYPH\s*et\s*EE\s*hyph_et$/ or print" %{dictdir}/dictionary.lst
fi

%post -n myspell-hyph-fi
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*fi[ \t]*FI[ \t]*hyph_fi" %{dictdir}/dictionary.lst; then
	echo "HYPH fi FI hyph_fi" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-hyph-fi
if [ "$1" = "0" ]; then
	perl -ni -e "/^HYPH\s*fi\s*FI\s*hyph_fi$/ or print" %{dictdir}/dictionary.lst
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
	perl -ni -e "/^HYPH\s*fr\s*FR\s*hyph_fr$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^HYPH\s*fr\s*BE\s*hyph_fr$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^HYPH\s*fr\s*CA\s*hyph_fr$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^HYPH\s*fr\s*LU\s*hyph_fr$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^HYPH\s*fr\s*MC\s*hyph_fr$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^HYPH\s*fr\s*CH\s*hyph_fr$/ or print" %{dictdir}/dictionary.lst
fi

%post -n myspell-hyph-ga
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*ga[ \t]*IE[ \t]*hyph_ga" %{dictdir}/dictionary.lst; then
	echo "HYPH ga IE hyph_ga" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-hyph-ga
if [ "$1" = "0" ]; then
	perl -ni -e "/^HYPH\s*ga\s*IE\s*hyph_ga$/ or print" %{dictdir}/dictionary.lst
fi

%post -n myspell-hyph-hu
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*hu[ \t]*HU[ \t]*hyph_hu" %{dictdir}/dictionary.lst; then
	echo "HYPH hu HU hyph_hu" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-hyph-hu
if [ "$1" = "0" ]; then
	perl -ni -e "/^HYPH\s*hu\s*HU\s*hyph_hu$/ or print" %{dictdir}/dictionary.lst
fi

%post -n myspell-hyph-id
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*id[ \t]*ID[ \t]*hyph_id" %{dictdir}/dictionary.lst; then
	echo "HYPH id ID hyph_id" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-hyph-id
if [ "$1" = "0" ]; then
	perl -ni -e "/^HYPH\s*id\s*ID\s*hyph_id$/ or print" %{dictdir}/dictionary.lst
fi

%post -n myspell-hyph-is
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*is[ \t]*IS[ \t]*hyph_is" %{dictdir}/dictionary.lst; then
	echo "HYPH is IS hyph_is" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-hyph-is
if [ "$1" = "0" ]; then
	perl -ni -e "/^HYPH\s*is\s*IS\s*hyph_is$/ or print" %{dictdir}/dictionary.lst
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
	perl -ni -e "/^HYPH\s*it\s*IT\s*hyph_it$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^HYPH\s*it\s*CH\s*hyph_it$/ or print" %{dictdir}/dictionary.lst
fi

%post -n myspell-hyph-lt
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*lt[ \t]*LT[ \t]*hyph_lt" %{dictdir}/dictionary.lst; then
	echo "HYPH lt LT hyph_lt" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-hyph-lt
if [ "$1" = "0" ]; then
	perl -ni -e "/^HYPH\s*lt\s*LT\s*hyph_lt$/ or print" %{dictdir}/dictionary.lst
fi

%post -n myspell-hyph-nl
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*nl[ \t]*NL[ \t]*hyph_nl" %{dictdir}/dictionary.lst; then
	echo "HYPH nl NL hyph_nl" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-hyph-nl
if [ "$1" = "0" ]; then
	perl -ni -e "/^HYPH\s*nl\s*NL\s*hyph_nl$/ or print" %{dictdir}/dictionary.lst
fi

%post -n myspell-hyph-pl
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*pl[ \t]*PL[ \t]*hyph_pl" %{dictdir}/dictionary.lst; then
	echo "HYPH pl PL hyph_pl" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-hyph-pl
if [ "$1" = "0" ]; then
	perl -ni -e "/^HYPH\s*pl\s*PL\s*hyph_pl$/ or print" %{dictdir}/dictionary.lst
fi

%post -n myspell-hyph-pt
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*pt[ \t]*PT[ \t]*hyph_pt" %{dictdir}/dictionary.lst; then
	echo "HYPH pt PT hyph_pt" >> %{dictdir}/dictionary.lst
fi

if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*pt[ \t]*BR[ \t]*hyph_pt" %{dictdir}/dictionary.lst; then
	echo "HYPH pt BR hyph_pt" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-hyph-pt
if [ "$1" = "0" ]; then
	perl -ni -e "/^HYPH\s*pt\s*PT\s*hyph_pt$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^HYPH\s*pt\s*BR\s*hyph_pt$/ or print" %{dictdir}/dictionary.lst
fi

%post -n myspell-hyph-ru
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*ru[ \t]*RU[ \t]*hyph_ru" %{dictdir}/dictionary.lst; then
	echo "HYPH ru RU hyph_ru" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-hyph-ru
if [ "$1" = "0" ]; then
	perl -ni -e "/^HYPH\s*ru\s*RU\s*hyph_ru$/ or print" %{dictdir}/dictionary.lst
fi

%post -n myspell-hyph-sk
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*sk[ \t]*SK[ \t]*hyph_sk" %{dictdir}/dictionary.lst; then
	echo "HYPH sk SK hyph_sk" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-hyph-sk
if [ "$1" = "0" ]; then
	perl -ni -e "/^HYPH\s*sk\s*SK\s*hyph_sk$/ or print" %{dictdir}/dictionary.lst
fi

%post -n myspell-hyph-sl
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*sl[ \t]*SI[ \t]*hyph_sl" %{dictdir}/dictionary.lst; then
	echo "HYPH sl SI hyph_sl" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-hyph-sl
if [ "$1" = "0" ]; then
	perl -ni -e "/^HYPH\s*sl\s*SI\s*hyph_sl$/ or print" %{dictdir}/dictionary.lst
fi

%post -n myspell-hyph-sv
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*sv[ \t]*SE[ \t]*hyph_sv" %{dictdir}/dictionary.lst; then
	echo "HYPH sv SE hyph_sv" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-hyph-sv
if [ "$1" = "0" ]; then
	perl -ni -e "/^HYPH\s*sv\s*SE\s*hyph_sv$/ or print" %{dictdir}/dictionary.lst
fi

%post -n myspell-hyph-uk
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^HYPH[ \t]*uk[ \t]*UA[ \t]*hyph_uk" %{dictdir}/dictionary.lst; then
	echo "HYPH uk UA hyph_uk" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-hyph-uk
if [ "$1" = "0" ]; then
	perl -ni -e "/^HYPH\s*uk\s*UA\s*hyph_uk$/ or print" %{dictdir}/dictionary.lst
fi

##
## Scripts for thesaurus
##
%post -n myspell-thes-bg_BG
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^THES[ \t]*bg[ \t]*BG[ \t]*th_bg_BG" %{dictdir}/dictionary.lst; then
	echo "THES bg BG th_bg_BG" >> %{dictdir}/dictionary.lst
fi
%preun -n myspell-thes-bg_BG
if [ "$1" = "0" ]; then
	perl -ni -e "/^THES\s*bg\s*BG\s*th_bg_BG$/ or print" %{dictdir}/dictionary.lst
fi

%post -n myspell-thes-de_DE
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^THES[ \t]*de[ \t]*DE[ \t]*th_de_DE" %{dictdir}/dictionary.lst; then
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
	perl -ni -e "/^THES\s*de\s*DE\s*th_de_DE$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^THES\s*de\s*AT\s*th_de_DE$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^THES\s*de\s*CH\s*th_de_DE$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^THES\s*de\s*LI\s*th_de_DE$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^THES\s*de\s*LU\s*th_de_DE$/ or print" %{dictdir}/dictionary.lst
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
	perl -ni -e "/^THES\s*en\s*US\s*th_en_US$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^THES\s*en\s*CA\s*th_en_US$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^THES\s*en\s*GB\s*th_en_US$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^THES\s*en\s*AU\s*th_en_US$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^THES\s*en\s*BZ\s*th_en_US$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^THES\s*en\s*IE\s*th_en_US$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^THES\s*en\s*JM\s*th_en_US$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^THES\s*en\s*NZ\s*th_en_US$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^THES\s*en\s*PH\s*th_en_US$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^THES\s*en\s*TT\s*th_en_US$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^THES\s*en\s*ZA\s*th_en_US$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^THES\s*en\s*ZW\s*th_en_US$/ or print" %{dictdir}/dictionary.lst
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
	perl -ni -e "/^THES\s*es\s*ES\s*th_es_ES$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^THES\s*es\s*AR\s*th_es_ES$/ or print" %{dictdir}/dictionary.lst
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
	perl -ni -e "/^THES\s*fr\s*FR\s*th_fr_FR$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^THES\s*fr\s*BE\s*th_fr_FR$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^THES\s*fr\s*CA\s*th_fr_FR$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^THES\s*fr\s*CH\s*th_fr_FR$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^THES\s*fr\s*LU\s*th_fr_FR$/ or print" %{dictdir}/dictionary.lst
	perl -ni -e "/^THES\s*fr\s*MC\s*th_fr_FR$/ or print" %{dictdir}/dictionary.lst
fi

%post -n myspell-thes-it_IT
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^THES[ \t]*it[ \t]*IT[ \t]*th_it_IT" %{dictdir}/dictionary.lst; then
	echo "THES it IT th_it_IT" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-thes-it_IT
if [ "$1" = "0" ]; then
	perl -ni -e "/^THES\s*it\s*IT\s*th_it_IT$/ or print" %{dictdir}/dictionary.lst
fi

%post -n myspell-thes-pl_PL
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^THES[ \t]*pl[ \t]*PL[ \t]*th_pl_PL" %{dictdir}/dictionary.lst; then
	echo "THES pl PL th_pl_PL" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-thes-pl_PL
if [ "$1" = "0" ]; then
	perl -ni -e "/^THES\s*pl\s*PL\s*th_pl_PL$/ or print" %{dictdir}/dictionary.lst
fi

%post -n myspell-thes-sk_SK
umask 002
if [ ! -f "%{dictdir}/dictionary.lst" ] || ! grep -q "^THES[ \t]*sk[ \t]*SK[ \t]*th_sk_SK" %{dictdir}/dictionary.lst; then
	echo "THES sk SK th_sk_SK" >> %{dictdir}/dictionary.lst
fi

%preun -n myspell-thes-sk_SK
if [ "$1" = "0" ]; then
	perl -ni -e "/^THES\s*sk\s*SK\s*th_sk_SK$/ or print" %{dictdir}/dictionary.lst
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

%files -n myspell-hr_HR
%defattr(644,root,root,755)
%doc doc/DICT/hr_HR/*
%{dictdir}/hr_HR.*

%files -n myspell-hu_HU
%defattr(644,root,root,755)
%doc doc/DICT/hu_HU/*
%{dictdir}/hu_HU.*

%files -n myspell-id_ID
%defattr(644,root,root,755)
%doc doc/DICT/id_ID/*
%{dictdir}/id_ID.*

%files -n myspell-it_IT
%defattr(644,root,root,755)
%doc doc/DICT/it_IT/*
%{dictdir}/it_IT.*

%files -n myspell-lt_LT
%defattr(644,root,root,755)
%doc doc/DICT/lt_LT/*
%{dictdir}/lt_LT.*

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


##
## Files for hyphenation
##
%files -n myspell-hyph-bg
%defattr(644,root,root,755)
%doc doc/HYPH/hyph_bg/*
%{dictdir}/hyph_bg.*

%files -n myspell-hyph-cs
%defattr(644,root,root,755)
%doc doc/HYPH/hyph_cs/*
%{dictdir}/hyph_cs.*

%files -n myspell-hyph-da
%defattr(644,root,root,755)
%doc doc/HYPH/hyph_da/*
%{dictdir}/hyph_da.*

%files -n myspell-hyph-de
%defattr(644,root,root,755)
%doc doc/HYPH/hyph_de/*
%{dictdir}/hyph_de.*

%files -n myspell-hyph-el
%defattr(644,root,root,755)
%doc doc/HYPH/hyph_el/*
%{dictdir}/hyph_el.*

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
%doc doc/HYPH/hyph_et/*
%{dictdir}/hyph_et.*

%files -n myspell-hyph-fi
%defattr(644,root,root,755)
%doc doc/HYPH/hyph_fi/*
%{dictdir}/hyph_fi.*

%files -n myspell-hyph-fr
%defattr(644,root,root,755)
%doc doc/HYPH/hyph_fr/*
%{dictdir}/hyph_fr.*

%files -n myspell-hyph-ga
%defattr(644,root,root,755)
%doc doc/HYPH/hyph_ga/*
%{dictdir}/hyph_ga.*

%files -n myspell-hyph-hu
%defattr(644,root,root,755)
%doc doc/HYPH/hyph_hu/*
%{dictdir}/hyph_hu.*

%files -n myspell-hyph-id
%defattr(644,root,root,755)
%doc doc/HYPH/hyph_id/*
%{dictdir}/hyph_id.*

%files -n myspell-hyph-is
%defattr(644,root,root,755)
%doc doc/HYPH/hyph_is/*
%{dictdir}/hyph_is.*

%files -n myspell-hyph-it
%defattr(644,root,root,755)
%doc doc/HYPH/hyph_it/*
%{dictdir}/hyph_it.*

%files -n myspell-hyph-lt
%defattr(644,root,root,755)
%doc doc/HYPH/hyph_lt/*
%{dictdir}/hyph_lt.*

%files -n myspell-hyph-nl
%defattr(644,root,root,755)
%doc doc/HYPH/hyph_nl/*
%{dictdir}/hyph_nl.*

%files -n myspell-hyph-pl
%defattr(644,root,root,755)
%doc doc/HYPH/hyph_pl/*
%{dictdir}/hyph_pl.*

%files -n myspell-hyph-pt
%defattr(644,root,root,755)
%doc doc/HYPH/hyph_pt/*
%{dictdir}/hyph_pt.*

%files -n myspell-hyph-ru
%defattr(644,root,root,755)
%doc doc/HYPH/hyph_ru/*
%{dictdir}/hyph_ru.*

%files -n myspell-hyph-sk
%defattr(644,root,root,755)
%doc doc/HYPH/hyph_sk/*
%{dictdir}/hyph_sk.*

%files -n myspell-hyph-sl
%defattr(644,root,root,755)
%doc doc/HYPH/hyph_sl/*
%{dictdir}/hyph_sl.*

%files -n myspell-hyph-sv
%defattr(644,root,root,755)
%doc doc/HYPH/hyph_sv/*
%{dictdir}/hyph_sv.*

%files -n myspell-hyph-uk
%defattr(644,root,root,755)
%doc doc/HYPH/hyph_uk/*
%{dictdir}/hyph_uk.*

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

Summary:	Skeleton package which defines a base of PLD system
Summary(pl):	Pakiet szkieletowy ktСry okre╤la podstawЙ systemu PLD
Summary(ru):	Базовый пакет, определяющий систему PLD Linux Distribution
Summary(uk):	Базовий пакет, який визнача╓ систему PLD Linux Distribution
Name:		basesystem
Version:	1.99
Release:	7
Epoch:		2
License:	GPL
Group:		Base
Requires:	FHS
Requires:	dev
Requires:	setup
Obsoletes:	vserver-basesystem
# obsoletes for removed packages
Obsoletes:	bdflush
Obsoletes:	gmc
Obsoletes:	gwp
Obsoletes:	xwpick
# GNOME 1.x stuff dropped in Ac
Obsoletes:	gda1-ldap
Obsoletes:	gda1-mysql
Obsoletes:	gda1-odbc
Obsoletes:	gda1-postgres
Obsoletes:	gnome-db
Obsoletes:	gnome-db-devel
Obsoletes:	gnome-db-static
Obsoletes:	libgda1-clientcpp
Obsoletes:	libgda1-clientcpp-devel
Obsoletes:	libgda1-devel
Obsoletes:	libgda1-static
Obsoletes:	libglade-gnomedb
Obsoletes:	libglade-gnomedb-devel
Obsoletes:	libglade-gnomedb-static
# no openoffice.org on those arches
%ifarch i386 i486 ppc sparc sparcv9
Obsoletes:	openoffice
Obsoletes:	openoffice-i18n-af
Obsoletes:	openoffice-i18n-af-gtk
Obsoletes:	openoffice-i18n-ar
Obsoletes:	openoffice-i18n-ar-gtk
Obsoletes:	openoffice-i18n-bg
Obsoletes:	openoffice-i18n-bg-gtk
Obsoletes:	openoffice-i18n-ca
Obsoletes:	openoffice-i18n-ca-gtk
Obsoletes:	openoffice-i18n-cs
Obsoletes:	openoffice-i18n-cs-gtk
Obsoletes:	openoffice-i18n-cy
Obsoletes:	openoffice-i18n-cy-gtk
Obsoletes:	openoffice-i18n-da
Obsoletes:	openoffice-i18n-da-gtk
Obsoletes:	openoffice-i18n-de
Obsoletes:	openoffice-i18n-de-gtk
Obsoletes:	openoffice-i18n-el
Obsoletes:	openoffice-i18n-el-gtk
Obsoletes:	openoffice-i18n-en
Obsoletes:	openoffice-i18n-en
Obsoletes:	openoffice-i18n-en-gtk
Obsoletes:	openoffice-i18n-en-kde
Obsoletes:	openoffice-i18n-es
Obsoletes:	openoffice-i18n-es-gtk
Obsoletes:	openoffice-i18n-et
Obsoletes:	openoffice-i18n-et-gtk
Obsoletes:	openoffice-i18n-eu
Obsoletes:	openoffice-i18n-eu-gtk
Obsoletes:	openoffice-i18n-eu-kde
Obsoletes:	openoffice-i18n-fa
Obsoletes:	openoffice-i18n-fa-gtk
Obsoletes:	openoffice-i18n-fa-kde
Obsoletes:	openoffice-i18n-fi
Obsoletes:	openoffice-i18n-fi-gtk
Obsoletes:	openoffice-i18n-fo
Obsoletes:	openoffice-i18n-fo-gtk
Obsoletes:	openoffice-i18n-fr
Obsoletes:	openoffice-i18n-fr-gtk
Obsoletes:	openoffice-i18n-ga
Obsoletes:	openoffice-i18n-ga-gtk
Obsoletes:	openoffice-i18n-gl
Obsoletes:	openoffice-i18n-gl-gtk
Obsoletes:	openoffice-i18n-he
Obsoletes:	openoffice-i18n-he-gtk
Obsoletes:	openoffice-i18n-hi
Obsoletes:	openoffice-i18n-hi-gtk
Obsoletes:	openoffice-i18n-hr
Obsoletes:	openoffice-i18n-hr-gtk
Obsoletes:	openoffice-i18n-hu
Obsoletes:	openoffice-i18n-hu-gtk
Obsoletes:	openoffice-i18n-ia
Obsoletes:	openoffice-i18n-ia-gtk
Obsoletes:	openoffice-i18n-id
Obsoletes:	openoffice-i18n-id-gtk
Obsoletes:	openoffice-i18n-it
Obsoletes:	openoffice-i18n-ja
Obsoletes:	openoffice-i18n-ja-gtk
Obsoletes:	openoffice-i18n-kn
Obsoletes:	openoffice-i18n-kn-gtk
Obsoletes:	openoffice-i18n-kn-kde
Obsoletes:	openoffice-i18n-ko
Obsoletes:	openoffice-i18n-ko-gtk
Obsoletes:	openoffice-i18n-la
Obsoletes:	openoffice-i18n-la-gtk
Obsoletes:	openoffice-i18n-lt
Obsoletes:	openoffice-i18n-lt-gtk
Obsoletes:	openoffice-i18n-med
Obsoletes:	openoffice-i18n-med-gtk
Obsoletes:	openoffice-i18n-mi
Obsoletes:	openoffice-i18n-mi-gtk
Obsoletes:	openoffice-i18n-ms
Obsoletes:	openoffice-i18n-ms-gtk
Obsoletes:	openoffice-i18n-nb
Obsoletes:	openoffice-i18n-nb-gtk
Obsoletes:	openoffice-i18n-nl
Obsoletes:	openoffice-i18n-nl-gtk
Obsoletes:	openoffice-i18n-nn
Obsoletes:	openoffice-i18n-nn-gtk
Obsoletes:	openoffice-i18n-nso
Obsoletes:	openoffice-i18n-nso-gtk
Obsoletes:	openoffice-i18n-pl
Obsoletes:	openoffice-i18n-pl-gtk
Obsoletes:	openoffice-i18n-pt
Obsoletes:	openoffice-i18n-pt-gtk
Obsoletes:	openoffice-i18n-pt_BR
Obsoletes:	openoffice-i18n-pt_BR-gtk
Obsoletes:	openoffice-i18n-ro
Obsoletes:	openoffice-i18n-ro-gtk
Obsoletes:	openoffice-i18n-ru
Obsoletes:	openoffice-i18n-ru-gtk
Obsoletes:	openoffice-i18n-sk
Obsoletes:	openoffice-i18n-sk-gtk
Obsoletes:	openoffice-i18n-sl
Obsoletes:	openoffice-i18n-sl-gtk
Obsoletes:	openoffice-i18n-sv
Obsoletes:	openoffice-i18n-sv-gtk
Obsoletes:	openoffice-i18n-th
Obsoletes:	openoffice-i18n-th-gtk
Obsoletes:	openoffice-i18n-th-kde
Obsoletes:	openoffice-i18n-tn
Obsoletes:	openoffice-i18n-tn-gtk
Obsoletes:	openoffice-i18n-tn-kde
Obsoletes:	openoffice-i18n-tr
Obsoletes:	openoffice-i18n-tr-gtk
Obsoletes:	openoffice-i18n-uk
Obsoletes:	openoffice-i18n-uk-gtk
Obsoletes:	openoffice-i18n-zh
Obsoletes:	openoffice-i18n-zh
Obsoletes:	openoffice-i18n-zh_CN
Obsoletes:	openoffice-i18n-zh_CN-gtk
Obsoletes:	openoffice-i18n-zh_TW
Obsoletes:	openoffice-i18n-zh_TW-gtk
Obsoletes:	openoffice-i18n-zu
Obsoletes:	openoffice-i18n-zu-gtk
Obsoletes:	openoffice-libs
Obsoletes:	openoffice-libs-gtk
Obsoletes:	openoffice-libs-kde
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
While this package does not contain any files, it does perform an
important function. It defines the components of a basic PLD
distribution, providing packages install in right order.

%description -l pl
Mimo ©e ten pakiet nie zawiera ©adnych plikСw, ma on bardzo wa©ne
zadanie. Definiuje komponenty podstawowej dystrybucji PLD, zapewniaj╠c
tym samym wЁa╤ciwy porz╠dek instalacji pakietСw.

%description -l ru
Хотя этот пакет и не содержит никаких файлов, он выполняет важную
функцию - определяет компоненты базовой системы PLD Linux
Distribution, такие как порядок установки пакетов в процессе
первоначальной инсталляции. Этот пакет должен устанавливаться в
систему первым и никогда не удаляться.

%description -l uk
Хоч цей пакет ╕ не м╕стить н╕яких файл╕в, в╕н викону╓ важливу функц╕ю
- визнача╓ компоненти базово╖ системи PLD Linux Distribution, так╕ як
посл╕довн╕сть встановлення пакет╕в в процес╕ початково╖ ╕нсталяц╕╖.
Цей пакет повинен встановлюватись у систему першим ╕ н╕коли не
видалятись.

%prep

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

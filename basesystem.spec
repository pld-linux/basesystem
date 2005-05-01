Summary:	Skeleton package which defines a base of PLD system
Summary(pl):	Pakiet szkieletowy ktСry okre╤la podstawЙ systemu PLD
Summary(ru):	Базовый пакет, определяющий систему PLD Linux Distribution
Summary(uk):	Базовий пакет, який визнача╓ систему PLD Linux Distribution
Name:		basesystem
Version:	1.99
Release:	4
Epoch:		2
License:	GPL
Group:		Base
PreReq:		FHS
PreReq:		setup
PreReq:		dev
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
# obsoletes for removed packages
Obsoletes:	bdflush
Obsoletes:	gmc
Obsoletes:	gwp
Obsoletes:	xwpick
%ifarch alpha
Obsoletes:	gfax
%endif
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

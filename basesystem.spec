Summary:	Skeleton package which defines a base of PLD system
Summary(pl):	Pakiet szkieletowy ktСry okre╤la podstawЙ systemu PLD
Summary(ru):	Базовый пакет, определяющий систему KSI Linux
Summary(uk):	Базовий пакет, який визнача╓ систему KSI Linux
Name:		basesystem
Version:	1.0
Release:	9
Epoch:		2
License:	GPL
Group:		Base
Prereq:		FHS
Prereq:		setup
Prereq:		dev
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

Obsoletes:	gmc
Obsoletes:	gwp
Obsoletes:	xwpick

%description
While this package does not contain any files, it does perform an
important function. It defines the components of a basic PLD
distribution, providing packages install in right order.

%description -l pl
Mimo ©e ten pakiet nie zawiera ©adnych plikСw, ma on bardzo wa©ne
zadanie. Definiuje komponenty podstawowej dystrybucji PLD, zapewniaj╠c
tym samym wЁa╤ciwy porz╠dek instalacji pakietСw.

%description -l uk
Хотя этот пакет и не содержит никаких файлов, он выполняет важную
функцию - определяет компоненты базовой системы KSI Linux, такие как
порядок установки пакетов в процессе первоначальной инсталляции. Этот
пакет должен устанавливаться в систему первым и никогда не удаляться.

%description -l ru
Хоч цей пакет ╕ не м╕стить н╕яких файл╕в, в╕н викону╓ важливу функц╕ю
- визнача╓ компоненти базово╖ системи KSI Linux, так╕ як посл╕довн╕сть
встановлення пакет╕в в процес╕ початково╖ ╕нсталяц╕╖. Цей пакет
повинен встановлюватись у систему першим ╕ н╕коли не видалятись.

%prep

%files
%defattr(644,root,root,755)

Summary:	Skeleton package which defines a base of PLD system
Summary(pl):	Pakiet szkieletowy który okre¶la podstawê systemu PLD
Name:		basesystem
Version:	1.0
Release:	5
Epoch:		1
Group:		Base
Group(pl):	Podstawowe
License:	GPL
Prereq:		FHS
Prereq:		setup
Prereq:		dev
#Requires:	rpm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
While this package does not contain any files, it does perform an
important function. It defines the components of a basic PLD
distribution, providing packages install in right order.

%description -l pl
Mimo ¿e ten pakiet nie zawiera ¿adnych plików, ma on bardzo wa¿ne
zadanie. Definiuje komponenty podstawowej dystrybucji PLD, zapewniaj±c
tym samym w³a¶ciwy porz±dek instalacji pakietów.

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

Summary:	Skeleton package which defines a base of PLD system
Summary(pl):	Pakiet szkieletowy kt�ry okre�la podstaw� systemu PLD
Name:		basesystem
Version:	1.0
Release:	1
Group:		Base
Group(pl):	Podstawowe
License:	GPL
Prereq:		FHS
Prereq:		setup
Prereq:		dev
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
While this package does not contain any files, it does perform an important
function. It defines the components of a basic PLD distribution, providing
packages install in right order.

%description -l pl
Mimo �e ten pakiet nie zawiera �adnych plik�w, ma on bardzo wa�ne zadanie.
Definiuje komponenty podstawowej dystrybucji PLD, zapewniaj�c tym samym
w�a�ciwy porz�dek instalacji pakiet�w.

%prep

%build

%install

%files
%defattr(644,root,root,755)

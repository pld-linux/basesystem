Summary:	Skeleton package which defines a base of PLD system
Summary(pl):	Pakiet szkieletowy kt�ry okre�la podstaw� systemu PLD
Summary(ru):	������� �����, ������������ ������� PLD Linux Distribution
Summary(uk):	������� �����, ���� �������� ������� PLD Linux Distribution
Name:		basesystem
Version:	2.99
Release:	2
Epoch:		2
License:	GPL
Group:		Base
Prereq:		FHS
Prereq:		setup
Prereq:		dev
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

# obsoletes for removed packages
Obsoletes:	gmc
Obsoletes:	gwp
Obsoletes:	xwpick
%ifarch alpha
Obsoletes:	gfax
%endif
Obsoletes:	gda1-ldap
Obsoletes:	gda1-mysql
Obsoletes:	gda1-odbc
Obsoletes:	gda1-postgres
Obsoletes:	libgda1-clientcpp
Obsoletes:	libgda1-clientcpp-devel
Obsoletes:	libgda1-devel
Obsoletes:	libgda1-static
Obsoletes:	gnome-db
Obsoletes:	gnome-db-devel
Obsoletes:	gnome-db-static
Obsoletes:	libglade-gnomedb
Obsoletes:	libglade-gnomedb-devel
Obsoletes:	libglade-gnomedb-static

%description
While this package does not contain any files, it does perform an
important function. It defines the components of a basic PLD
distribution, providing packages install in right order.

%description -l pl
Mimo �e ten pakiet nie zawiera �adnych plik�w, ma on bardzo wa�ne
zadanie. Definiuje komponenty podstawowej dystrybucji PLD, zapewniaj�c
tym samym w�a�ciwy porz�dek instalacji pakiet�w.

%description -l ru
���� ���� ����� � �� �������� ������� ������, �� ��������� ������
������� - ���������� ���������� ������� ������� PLD Linux
Distribution, ����� ��� ������� ��������� ������� � ��������
�������������� �����������. ���� ����� ������ ��������������� �
������� ������ � ������� �� ���������.

%description -l uk
��� ��� ����� � �� ͦ����� Φ���� ���̦�, צ� �����դ ������� ����æ�
- �������� ���������� �����ϧ ������� PLD Linux Distribution, ��˦ ��
���̦���Φ��� ������������ ����Ԧ� � �����Ӧ ��������ϧ �������æ�.
��� ����� ������� ��������������� � ������� ������ � Φ���� ��
����������.

%prep

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

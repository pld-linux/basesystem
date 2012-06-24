Summary:	Skeleton package which defines a base of PLD system
Summary(pl):	Pakiet szkieletowy kt�ry okre�la podstaw� systemu PLD
Summary(ru):	������� �����, ������������ ������� KSI Linux
Summary(uk):	������� �����, ���� �������� ������� KSI Linux
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
Mimo �e ten pakiet nie zawiera �adnych plik�w, ma on bardzo wa�ne
zadanie. Definiuje komponenty podstawowej dystrybucji PLD, zapewniaj�c
tym samym w�a�ciwy porz�dek instalacji pakiet�w.

%description -l uk
���� ���� ����� � �� �������� ������� ������, �� ��������� ������
������� - ���������� ���������� ������� ������� KSI Linux, ����� ���
������� ��������� ������� � �������� �������������� �����������. ����
����� ������ ��������������� � ������� ������ � ������� �� ���������.

%description -l ru
��� ��� ����� � �� ͦ����� Φ���� ���̦�, צ� �����դ ������� ����æ�
- �������� ���������� �����ϧ ������� KSI Linux, ��˦ �� ���̦���Φ���
������������ ����Ԧ� � �����Ӧ ��������ϧ �������æ�. ��� �����
������� ��������������� � ������� ������ � Φ���� �� ����������.

%prep

%files
%defattr(644,root,root,755)

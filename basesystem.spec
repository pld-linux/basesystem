Summary:	Skeleton package which defines a base of PLD system
Summary(pl.UTF-8):	Pakiet szkieletowy który określa podstawę systemu PLD
Summary(ru.UTF-8):	Базовый пакет, определяющий систему PLD Linux Distribution
Summary(uk.UTF-8):	Базовий пакет, який визначає систему PLD Linux Distribution
Name:		basesystem
Version:	2.99
Release:	5
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
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_enable_debug_packages	0

%description
While this package does not contain any files, it does perform an
important function. It defines the components of a basic PLD
distribution, providing packages install in right order.

%description -l pl.UTF-8
Mimo że ten pakiet nie zawiera żadnych plików, ma on bardzo ważne
zadanie. Definiuje komponenty podstawowej dystrybucji PLD, zapewniając
tym samym właściwy porządek instalacji pakietów.

%description -l ru.UTF-8
Хотя этот пакет и не содержит никаких файлов, он выполняет важную
функцию - определяет компоненты базовой системы PLD Linux
Distribution, такие как порядок установки пакетов в процессе
первоначальной инсталляции. Этот пакет должен устанавливаться в
систему первым и никогда не удаляться.

%description -l uk.UTF-8
Хоч цей пакет і не містить ніяких файлів, він виконує важливу функцію
- визначає компоненти базової системи PLD Linux Distribution, такі як
послідовність встановлення пакетів в процесі початкової інсталяції.
Цей пакет повинен встановлюватись у систему першим і ніколи не
видалятись.

%prep

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

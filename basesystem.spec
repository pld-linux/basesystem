Summary:	The skeleton package which defines a simple PLD Linux system.
Name:		basesystem
Version:	0.1
Release:	1
Copyright:	public domain
Group:		Base
Group(pl):      Podstawowe
Prereq:		setup filesystem dev
BuildRoot:	/tmp/%{name}-%{version}-root
BuildArchitectures:	noarch

%description
Basesystem defines the components of a basic PLD system (for example, the
package installation order to use during bootstrapping). Basesystem should
be the first package installed on a system, and it should never be removed.


%files
%defattr(644,root,root,755)

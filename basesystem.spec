Summary:	Skeleton package which defines a base of PLD system
Summary(pl.UTF-8):	Pakiet szkieletowy który określa podstawę systemu PLD
Summary(ru.UTF-8):	Базовый пакет, определяющий систему PLD Linux Distribution
Summary(uk.UTF-8):	Базовий пакет, який визначає систему PLD Linux Distribution
Name:		basesystem
Version:	2.0
Release:	5
Epoch:		2
License:	GPL
Group:		Base
Requires:	FHS
Requires:	dev
Requires:	setup
Provides:	systemd-units = 38
Obsoletes:	vserver-basesystem
# obsoletes for removed packages
Obsoletes:	bdflush
Obsoletes:	gmc
Obsoletes:	goobox
Obsoletes:	gst-editor
Obsoletes:	gstreamer-libdvdread
Obsoletes:	gstreamer-player
Obsoletes:	gstreamer-player-devel
Obsoletes:	gstreamer-player-nautilus
Obsoletes:	gstreamer-plugins
Obsoletes:	gstreamer08x
Obsoletes:	gstreamer08x-GConf
Obsoletes:	gstreamer08x-GConf-devel
Obsoletes:	gstreamer08x-a52dec
Obsoletes:	gstreamer08x-aac
Obsoletes:	gstreamer08x-artsd
Obsoletes:	gstreamer08x-audio-effects
Obsoletes:	gstreamer08x-audio-formats
Obsoletes:	gstreamer08x-audiofile
Obsoletes:	gstreamer08x-audiosink-alsa
Obsoletes:	gstreamer08x-audiosink-esd
Obsoletes:	gstreamer08x-audiosink-oss
Obsoletes:	gstreamer08x-cairo
Obsoletes:	gstreamer08x-cdaudio
Obsoletes:	gstreamer08x-cdio
Obsoletes:	gstreamer08x-cdparanoia
Obsoletes:	gstreamer08x-colorspace
Obsoletes:	gstreamer08x-devel
Obsoletes:	gstreamer08x-dirac
Obsoletes:	gstreamer08x-dts
Obsoletes:	gstreamer08x-dv
Obsoletes:	gstreamer08x-festival
Obsoletes:	gstreamer08x-flac
Obsoletes:	gstreamer08x-gdkpixbuf
Obsoletes:	gstreamer08x-gnomevfs
Obsoletes:	gstreamer08x-gsm
Obsoletes:	gstreamer08x-imagesink-gl
Obsoletes:	gstreamer08x-imagesink-x
Obsoletes:	gstreamer08x-imagesink-xv
Obsoletes:	gstreamer08x-interleave
Obsoletes:	gstreamer08x-jack
Obsoletes:	gstreamer08x-ladspa
Obsoletes:	gstreamer08x-lame
Obsoletes:	gstreamer08x-libdvdnav
Obsoletes:	gstreamer08x-libdvdread
Obsoletes:	gstreamer08x-libfame
Obsoletes:	gstreamer08x-libpng
Obsoletes:	gstreamer08x-libvisual
Obsoletes:	gstreamer08x-mad
Obsoletes:	gstreamer08x-mikmod
Obsoletes:	gstreamer08x-mjpegtools
Obsoletes:	gstreamer08x-mms
Obsoletes:	gstreamer08x-mpeg
Obsoletes:	gstreamer08x-musepack
Obsoletes:	gstreamer08x-musicbrainz
Obsoletes:	gstreamer08x-nas
Obsoletes:	gstreamer08x-pango
Obsoletes:	gstreamer08x-raw1394
Obsoletes:	gstreamer08x-shout2
Obsoletes:	gstreamer08x-sid
Obsoletes:	gstreamer08x-snapshot
Obsoletes:	gstreamer08x-sndfile
Obsoletes:	gstreamer08x-speex
Obsoletes:	gstreamer08x-static
Obsoletes:	gstreamer08x-swfdec
Obsoletes:	gstreamer08x-theora
Obsoletes:	gstreamer08x-vcd
Obsoletes:	gstreamer08x-video-effects
Obsoletes:	gstreamer08x-videosink-aa
Obsoletes:	gstreamer08x-videosink-directfb
Obsoletes:	gstreamer08x-videosink-libcaca
Obsoletes:	gstreamer08x-videosink-sdl
Obsoletes:	gstreamer08x-visualisation
Obsoletes:	gstreamer08x-vorbis
Obsoletes:	gstreamer08x-wavpack
Obsoletes:	gstreamer08x-xvid
Obsoletes:	gwp
Obsoletes:	jamboree
Obsoletes:	lindele
Obsoletes:	monkey-bubble
Obsoletes:	perl-SWF-Builder
Obsoletes:	python-gstreamer08x
Obsoletes:	python-pyflac
Obsoletes:	sonic-rainbow
Obsoletes:	xwpick
# wine was dropped on i386 due to lack of tls/nptl in glibc
# which makes it completly unusable (99% of programs are crashing)
%ifarch i386
Obsoletes:	wine
Obsoletes:	wine-devel
Obsoletes:	wine-dll-d3d
Obsoletes:	wine-dll-gl
Obsoletes:	wine-dll-twain
Obsoletes:	wine-drv-alsa
Obsoletes:	wine-drv-arts
Obsoletes:	wine-drv-jack
Obsoletes:	wine-drv-nas
Obsoletes:	wine-programs
Obsoletes:	winetools
Obsoletes:	xwine
%endif
# tyrex was dropped on architectures without java/jre
%ifarch alpha i386 sparc ppc
Obsoletes:	tyrex
%endif
# opera-i18n dropped on architectures without opera
%ifarch alpha %{x8664}
Obsoletes:	opera-i18n
%endif
# autopano-sift and muine have broken mono deps on alpha
%ifarch alpha
Obsoletes:	autopano-sift
Obsoletes:	muine
%endif
# laptop-mode-tools* was dropped on architectures without apmd
%ifarch alpha %{x8664} sparc
Obsoletes:	laptop-mode-tools
Obsoletes:	laptop-mode-tools-acpi
Obsoletes:	laptop-mode-tools-apm
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

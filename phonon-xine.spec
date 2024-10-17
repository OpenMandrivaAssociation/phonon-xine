Name: phonon-xine
Summary: Xine backend to Phonon
Version: 4.4.4
Release: %mkrel 2
Epoch: 2
Group: Sound
License: LGPLv2+
URL: https://phonon.kde.org
Source0: ftp://ftp.kde.org/pub/kde/stable/phonon/phonon-backend-xine/%version/phonon-backend-xine-%version.tar.bz2
BuildRequires: libxine-devel
BuildRequires: libxcb-devel
BuildRequires: kde4-macros
BuildRequires: automoc
BuildRequires: phonon-devel >= 2:4.4.4
Obsoletes: kde4-phonon-xine < 1:3.93.0-0.714129.2
Requires: xine-plugins
Suggests: xine-pulse
Provides: phonon-backend

%description
Xine backend to Phonon.

%files
%defattr(-,root,root)
%dir %_kde_libdir/kde4/plugins/phonon_backend
%_kde_libdir/kde4/plugins/phonon_backend/phonon_xine.so
%_kde_datadir/kde4/services/phononbackends/xine.desktop
%_kde_iconsdir/*/*/*/phonon-xine.*

#--------------------------------------------------------------------

%prep
%setup -qn phonon-backend-xine-%version

%build
%cmake_kde4
%make

%install
rm -fr %buildroot
%makeinstall_std -C build

%clean
rm -rf "%{buildroot}"


Name: kwin-scripts
Version: 2024.06.12
Release: 1
Source0: https://gitlab.com/Worldblender/kwin-scripts/-/archive/master/kwin-scripts-master.tar.bz2#/kwin-scripts-%{version}.tar.bz2
Summary: KWin scripts allowing to show coordinates while moving/resizing windows
URL: https://github.com/kwin-scripts/kwin-scripts
License: GPL-2.0+
Group: Graphical desktop/KDE
BuildArch: noarch
Supplements: plasma6-kwin

%description
KWin scripts allowing to show coordinates while moving/resizing windows

%package -n kwin5-scripts
Summary: KWin 5.x scripts allowing to show coordinates while moving/resizing windows
Supplements: kwin

%description -n kwin5-scripts
KWin 5.x scripts allowing to show coordinates while moving/resizing windows

%prep
%autosetup -p1 -n %{name}-master

%install
mkdir -p %{buildroot}%{_datadir}/kwin/scripts
cp -a windowgeometryinfo windowgeometryinfo6 %{buildroot}%{_datadir}/kwin/scripts/

%files
%{_datadir}/kwin/scripts/windowgeometryinfo6

%files -n kwin5-scripts
%{_datadir}/kwin/scripts/windowgeometryinfo

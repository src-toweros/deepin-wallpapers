%global md5() {$(echo -n %1 | md5sum | awk '{print$1}')}

Name:           deepin-wallpapers
Version:        1.6.14
Release:        2
Summary:        Deepin Wallpapers provides wallpapers of dde
License:        GPLv3
URL:            https://github.com/linuxdeepin/deepin-wallpapers
Source0:        %{name}_%{version}.orig.tar.xz
BuildArch:      noarch
BuildRequires:  dde-api

%description
%{summary}.

%prep
%setup -q -n %{name}-%{version}

%build
%make_build

%install
install -d %{buildroot}%{_datadir}/wallpapers/deepin/
cp deepin/* %{buildroot}%{_datadir}/wallpapers/deepin/

install -d %{buildroot}%{_var}/cache/
cp -ar image-blur %{buildroot}%{_var}/cache/

install -d %{buildroot}%{_datadir}/backgrounds/
ln -sv ../wallpapers/deepin/desktop.jpg %{buildroot}%{_datadir}/backgrounds/default_background.jpg
%files
%doc README.md
%{_datadir}/backgrounds/
%{_datadir}/wallpapers/deepin/
%{_var}/cache/image-blur/

%changelog
* Fri Aug 27 2021 konglidong <konglidong@uniontech.com> - 1.6.14-2
- fix build error

* Thu Jul 30 2020 openEuler Buildteam <buildteam@openeuler.org> - 1.6.14-1
- Package init

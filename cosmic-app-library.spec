%undefine _debugsource_packages
%define         appname com.system76.CosmicAppLibrary
Name:           cosmic-applibrary
Version:        1.0.0
%define beta alpha.7
Release:        %{?beta:0.%{beta}.}1
Summary:        A template for getting started with COSMIC
Group:          Desktop/COSMIC
License:        GPL-3.0-only
URL:            https://github.com/pop-os/cosmic-applibrary
Source0:        https://github.com/pop-os/cosmic-applibrary/archive/epoch-%{version}%{?beta:-%{beta}}/%{name}-epoch-%{version}%{?beta:-%{beta}}.tar.gz
Source1:        vendor.tar.xz
Source2:        cargo_config
BuildRequires:  rust-packaging
BuildRequires:  hicolor-icon-theme
BuildRequires:  just
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xkbcommon)

%description
Cosmic App Library is an application launcher for the COSMIC desktop that lists
all installed applications in a grid.

%prep
%autosetup -n %{name}-epoch-%{version}%{?beta:-%{beta}} -a1 -p1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
just build-release

%install
just rootdir=%{buildroot} prefix=%{_prefix} install

%files
%license LICENSE.md
%doc README.md
%{_bindir}/cosmic-app-library
%{_datadir}/applications/%{appname}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{appname}.svg
%{_datadir}/metainfo/%{appname}.metainfo.xml

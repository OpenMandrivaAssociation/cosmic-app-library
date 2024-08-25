%define         appname com.system76.CosmicAppLibrary
Name:           cosmic-app-library
Version:        1.0.0~alpha1
Release:        0
Summary:        A template for getting started with COSMIC
License:        GPL-3.0-only
URL:            https://github.com/pop-os/cosmic-applibrary
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  hicolor-icon-theme
BuildRequires:  just
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xkbcommon)

%description
Cosmic App Library is an application launcher for the COSMIC desktop that lists
all installed applications in a grid.

%prep
%autosetup -a1

%build
just build-release

%install
just rootdir=%{buildroot} prefix=%{_prefix} install
%suse_update_desktop_file %{appname}

%check
%{cargo_test}

%files
%license LICENSE.md
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{appname}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{appname}.svg
%{_datadir}/metainfo/%{appname}.metainfo.xml

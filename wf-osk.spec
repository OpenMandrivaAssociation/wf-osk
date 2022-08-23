Name:           wf-osk
Version:        0.1
Release:        1
Summary:        A very, very basic on-screen keyboard using gtkmm, virtual-keyboard-v1 and layer-shell protocols
License:        MIT
URL:            https://github.com/WayfireWM/wf-osk
Source0:        hhttps://github.com/WayfireWM/wf-osk/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildRequires:  meson
BuildRequires:  pkgconfig(gtk-layer-shell-0)
BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  pkgconfig(wayfire)
BuildRequires:  pkgconfig(wf-config)
BuildRequires:  pkgconfig(wlroots)
BuildRequires:  pkgconfig(wayland-protocols)

%description
Additional plugins for Wayfire
The plugins that come here are plugins that have external dependencies, for ex. giomm.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files

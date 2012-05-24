Summary:	Smart MUltipleXed Irc
Name:		smuxi
Version:	0.8.9.2
Release:	1
License:	GPLv2
Group:		Networking/IRC
URL:		http://www.smuxi.org
Source0:	http://smuxi.meebey.net/jaws/data/files/%{name}-%{version}.tar.gz

BuildRequires:	intltool
BuildRequires:	mono-devel
BuildRequires:	mono(System.Web.Extensions)
BuildRequires:	pkgconfig(dbus-sharp-1.0)
BuildRequires:	pkgconfig(dbus-sharp-glib-1.0)
BuildRequires:	pkgconfig(glade-sharp-2.0)
BuildRequires:	pkgconfig(glib-sharp-2.0)
BuildRequires:	pkgconfig(gtk-sharp-2.0)
BuildRequires:	pkgconfig(log4net)
BuildRequires:	pkgconfig(nini-1.1)
BuildRequires:	pkgconfig(notify-sharp)

Requires:	%{name}-frontend-gnome-irc = %{version}
Suggests:	%{name}-server = %{version}


%description
Smuxi is an irssi-inspired, flexible, user-friendly and cross-platform IRC 
client for advanced users, targeting the GNOME desktop.

%package engine
Summary:	Smart MUltipleXed Irc - Engine
Group:		Networking/IRC

%description engine
Engine for Smuxi

Smuxi is an irssi-inspired, flexible, user-friendly and cross-platform IRC client for advanced users, targeting the GNOME desktop.

%package engine-irc
Summary:	Smart MUltipleXed Irc - IRC Engine
Group:		Networking/IRC
Requires:	%{name}-engine = %{version}

%description engine-irc
IRC Engine for Smuxi

Smuxi is an irssi-inspired, flexible, user-friendly and cross-platform IRC client for advanced users, targeting the GNOME desktop.

%package frontend
Summary:	Smart MUltipleXed Irc - Engine
Group:		Networking/IRC
Requires:	%{name}-engine = %{version}

%description frontend
Frontend Library for Smuxi

Smuxi is an irssi-inspired, flexible, user-friendly and cross-platform IRC client for advanced users, targeting the GNOME desktop.

%package frontend-gnome
Summary:	Smart MUltipleXed Irc - Engine
Group:		Networking/IRC
Requires:	%{name}-frontend = %{version}

%description frontend-gnome
GNOME Frontend for Smuxi

Smuxi is an irssi-inspired, flexible, user-friendly and cross-platform IRC client for advanced users, targeting the GNOME desktop.

%package frontend-gnome-irc
Summary:	Smart MUltipleXed Irc - Engine
Group:		Networking/IRC
Requires:	%{name}-frontend-gnome = %{version}

%description frontend-gnome-irc
IRC Library for GNOME Frontent for Smuxi

Smuxi is an irssi-inspired, flexible, user-friendly and cross-platform IRC client for advanced users, targeting the GNOME desktop.

%package server
Summary:	Smart MUltipleXed Irc - Engine
Group:		Networking/IRC
Requires:	%{name}-engine = %{version}

%description server
Smuxi Server

Smuxi is an irssi-inspired, flexible, user-friendly and cross-platform IRC client for advanced users, targeting the GNOME desktop.

%prep
%setup -q

%build
%configure2_5x

%make

%install
%makeinstall_std

rm -f %{buildroot}%{_prefix}/lib/pkgconfig/*.pc

%find_lang %{name}-engine
%find_lang %{name}-engine-irc
%find_lang %{name}-frontend
%find_lang %{name}-frontend-gnome
%find_lang %{name}-frontend-gnome-irc
%find_lang %{name}-server

mkdir -p %{buildroot}%{_datadir}/applications

%files
%doc BUGS TODO FEATURES README CREDITS
%dir %{_prefix}/lib/%{name}

%files engine -f %{name}-engine.lang
%{_prefix}/lib/%{name}/Nini.dll
%{_prefix}/lib/%{name}/%{name}-engine*.dll*
%{_prefix}/lib/%{name}/%{name}-common.dll*

%files engine-irc -f %{name}-engine-irc.lang
%{_prefix}/lib/%{name}/%{name}-engine-irc*.dll*
%{_prefix}/lib/%{name}/Twitterizer2.dll*
%{_prefix}/lib/%{name}/Newtonsoft.Json.dll*
%{_prefix}/lib/%{name}/Meebey.SmartIrc4net.dll*

%files frontend -f %{name}-frontend.lang
%{_prefix}/lib/%{name}/%{name}-frontend.dll*

%files frontend-gnome -f %{name}-frontend-gnome.lang
%{_bindir}/%{name}-frontend-gnome
%{_prefix}/lib/%{name}/%{name}-frontend-gnome.exe*
%{_datadir}/applications/%{name}-frontend-gnome.desktop
%{_datadir}/pixmaps/smuxi-frontend-gnome.svg

%files frontend-gnome-irc -f %{name}-frontend-gnome-irc.lang
%{_prefix}/lib/%{name}/%{name}-frontend-gnome-irc.dll*

%files server -f %{name}-server.lang
%{_bindir}/%{name}-server
%{_prefix}/lib/%{name}/%{name}-server.exe*


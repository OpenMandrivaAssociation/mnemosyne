Name:		mnemosyne
Summary:	Flash-card learning tool
Version:	2.2.1
Release:	2
URL:		http://www.mnemosyne-proj.org/
Source0:	%{name}-%{version}.tar.gz
Patch0:		%{name}-desktop.patch
License:	GPLv2+
Group:		Education
BuildRequires:	desktop-file-utils
BuildRequires:	python-devel
BuildRequires:	python-setuptools
BuildArch:	noarch
Requires:	hicolor-icon-theme
Requires:	pygame
Requires:	python-qt4
Requires:	python-imaging
Requires:	python-matplotlib-qt4
Requires:	python-cherrypy

%description
Mnemosyne resembles a traditional flash-card program but with an
important twist: it uses a sophisticated algorithm to schedule the best
time for a card to come up for review.

Optional dependencies:
* latex: enables entering formulas using latex syntax.

%prep
%setup -q -n Mnemosyne-%{version}
%patch0 -p1 -b .d

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

install -d %{buildroot}%{_datadir}/applications
desktop-file-install --vendor="" \
	--dir=%{buildroot}%{_datadir}/applications \
	%{name}.desktop

install -d %{buildroot}/%{_datadir}/icons/hicolor/128x128/apps
pushd %{buildroot}/%{_datadir}/icons
mv %{name}.png hicolor/128x128/apps/%{name}.png
popd

%find_lang %{name}

%files -f %{name}.lang
%doc ChangeLog README
%{_bindir}/%{name}
%{_bindir}/%{name}-webserver
%{python_sitelib}/%{name}
%{python_sitelib}/Mnemosyne-%{version}-*.egg-info
%{python_sitelib}/openSM2sync
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png


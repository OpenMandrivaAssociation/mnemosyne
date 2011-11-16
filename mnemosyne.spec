Name:		mnemosyne
Summary:	Flash-card learning tool
Version:	1.2.2
Release:	%mkrel 1
URL:		http://www.mnemosyne-proj.org/
Source0:	http://downloads.sourceforge.net/sourceforge/mnemosyne-proj/%{name}-%{version}.tgz
Patch0:		%{name}-desktop.patch
License:	GPLv2+
Group:		Education
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	desktop-file-utils
BuildRequires:	python-devel
BuildRequires:	python-setuptools
BuildArch:	noarch
Requires:	hicolor-icon-theme
Requires:	pygame
Requires:	PyQt
Requires:	python-imaging

%description
Mnemosyne resembles a traditional flash-card program but with an
important twist: it uses a sophisticated algorithm to schedule the best
time for a card to come up for review.

Optional dependencies:
* latex: enables entering formulas using latex syntax.

%prep
%setup -q
%patch0 -p1 -b .d

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
rm -rf %{buildroot}

%{__python} setup.py install -O1 --skip-build --root %{buildroot}

install -d %{buildroot}%{_datadir}/applications
desktop-file-install --vendor="" \
	--dir=%{buildroot}%{_datadir}/applications \
	%{name}.desktop

install -d %{buildroot}/%{_datadir}/icons/hicolor/128x128/apps
pushd %{buildroot}/%{_datadir}/icons
mv %{name}.png hicolor/128x128/apps/%{name}.png
popd

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog LICENSE README
%{_bindir}/%{name}
%{python_sitelib}/%{name}
%{python_sitelib}/Mnemosyne-%{version}-*.egg-info
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png


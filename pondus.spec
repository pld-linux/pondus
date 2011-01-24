Summary:	Personal weight management program
Summary(pl.UTF-8):	Program do zarządzania własną wagą
Name:		pondus
Version:	0.7.3
Release:	1
License:	GPL v3+
Group:		X11/Applications
Source0:	http://bitbucket.org/eike/pondus/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	16108e66b33c97cd8c1393b1ae5222d6
Patch0:		%{name}-desktop.patch
URL:		http://www.ephys.de/software/pondus/
BuildRequires:	python-devel >= 2.4
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-matplotlib
Requires:	python-pygtk-gtk >= 2.12
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pondus is a personal weight management program written in Python and
Gtk+2. It aims to be simple to use, lightweight and fast. The data can
be plotted to get a quick overview of the history of your weight. A
simple weight planner allows to define "target weights".

%description -l pl.UTF-8
Pondus jest programem napisanym w Pythonie i Gtk+2 do zarządzania
własną wagą. Ma on być łatwy w obsłudze, lekki i szybki. Dane mogą być
przedstawione na wykresie, co umożliwia szybki przegląd historii wagi
użytkownika. Prosty planista wagi umożliwia zdefiniowanie "zamierzonej
wagi".

%prep
%setup -q
%patch0 -p1

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS CONTRIBUTING NEWS README TODO
%attr(755,root,root) %{_bindir}/pondus
%dir %{_datadir}/pondus
%{_datadir}/pondus/plot.png
%{_desktopdir}/pondus.desktop
%{_iconsdir}/hicolor/48x48/apps/pondus.png
%{_iconsdir}/hicolor/scalable/apps/pondus.svg
%{_mandir}/man1/pondus.1*
%{_pixmapsdir}/pondus.xpm
%dir %{py_sitescriptdir}/pondus
%{py_sitescriptdir}/pondus/*.py[co]
%dir %{py_sitescriptdir}/pondus/core
%{py_sitescriptdir}/pondus/core/*.py[co]
%dir %{py_sitescriptdir}/pondus/gui
%{py_sitescriptdir}/pondus/gui/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/pondus-*.egg-info
%endif

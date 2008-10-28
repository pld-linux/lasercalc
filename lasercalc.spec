#
Summary:	LaserCalc is application for the calculation of optical beam
Summary(pl.UTF-8):	LaserCalc jest aplikacją do kalkulacji promieni
Name:		lasercalc
Version:	0.1
Release:	0.1
License:	GPL v3
Group:		Applications/Engineering
Source0:	http://dl.sourceforge.net/lasercalc/%{name}-%{version}.tar.gz
# Source0-md5:	ecb6e1a395132c4a10b6141a17cc9b72
URL:		http://lasercalc.sourceforge.net/
BuildRequires:	gtkmm-devel
BuildRequires:	libglademm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LaserCalc is an Open Source Gnome application for the calculation of
optical beam paths and laser resonators based on Gaussian beam matrix
optics. In addition beam paths can be optimized to match given beam
parameters (mode matching).

%description -l pl.UTF-8
LaserCalc jest aplikacją Open Source przygotowaną dla środowiska Gnome
służącą do kalkulacji ścieżek promieni optycznych i rezonatorów
laserowych opartych o macierze wiązek optycznych Gaussa. Dodatkowo
ścieżki optyczne mogą być optymalizowane według zadanych parametrów
(mode matching).

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# remove bogus docdir
rm -fr $RPM_BUILD_ROOT%{_prefix}/doc/lasercalc

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README doc/*.{pdf,png,tex}
%attr(755,root,root) %{_bindir}/lasercalc
%dir %{_datadir}/%{name}/glade
%{_datadir}/%{name}/glade/*.glade

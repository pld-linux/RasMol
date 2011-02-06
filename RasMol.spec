# NOTE: new version at ftp://ftp.bernstein-plus-sons.com/software/RasMol_2.7.3.tar.gz
Summary:	Molecular graphics visualisation tool
Summary(pl.UTF-8):	Program do graficznej wizualizacji molekuł
Summary(ru.UTF-8):	Инструмент для визуализации молекулярных структур
Summary(uk.UTF-8):	Інструмент для візуалізації молекулярних структур
Name:		RasMol
Version:	2.7.2.1.1
Release:	1
License:	distributable
Group:		X11/Applications
Source0:	http://www.bernstein-plus-sons.com/software/%{name}_%{version}.tar.gz
# Source0-md5:	c75f1a30030b9a0ed0b55a076b1f235c
URL:		http://www.rasmol.org/
BuildRequires:	X11-devel
Obsoletes:	RasMol2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RasMol2 is a molecular graphics program intended for the visualisation
of proteins, nucleic acids and small molecules. The program is aimed
at display, teaching and generation of publication quality images.
RasMol runs on Microsoft Windows, Apple Macintosh, UNIX and VMS
systems. The UNIX and VMS systems require an 8, 24 or 32 bit colour X
Window System display (X11R4 or later). The program reads in a
molecule co-ordinate file and interactively displays the molecule on
the screen in a variety of colour schemes and molecule
representations. Currently available representations include
depth-cued wireframes, 'Dreiding' sticks, spacefilling (CPK) spheres,
ball and stick, solid and strand biomolecular ribbons, atom labels and
dot surfaces.

%description -l pl.UTF-8
RasMol2 to program do grafiki molekularnej mający służyć do
wizualizacji białek, kwasów nukleinowych i małych cząsteczek. Celem
programu jest wyświetlanie, nauka i generowanie obrazków o jakości
nadającej się do publikacji. RasMol działa na systemach Microsoft
Windows, Apple Macintosh, UNIX i VMS. Syystemy UNIX i VMS wymagają 8,
24 lub 32-bitowego ekranu systemu X Window (w wersji X11R4 lub
nowszej). Program czyta plik współrzędnych cząsteczek i interaktywnie
wyświetla cząsteczkę na ekranie w różnych schematach kolorów i
reprezentacji. Aktualnie dostępne reprezentacje obejmują model drutowy
odtwarzający głębokość, cylindryczne pałąki (Dreiding), sfery
wypełniające przestrzeń (CPK), kulki i pałąki, bryły i splecione
wstęgi biomolekularne, etykiety atomów i kropkowane powierzchnie.

%description -l ru.UTF-8
RasMol - программа молекулярной графики, используемая для визуализации
протеинов, нуклеиновых кислот и небольших молекул. Пригодна для
отображения, обучения и генерации изображений для публикаций.

%description -l uk.UTF-8
RasMol - програма молекулярної графіки, що застосовується для
візуалізації протеїнів, нуклеїнових кислот та невеликих молекул.
Придатна до відображення, навчання та генерації зображень для
публікацій.

%prep
%setup -q -n %{name}_%{version}

%build
cd src
xmkmf
%{__make} \
	CDEBUGFLAGS="%{rpmcflags}" \
	RASMOLDIR=%{_libdir}/rasmol

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1

cd src
%{__make} install install.man \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=%{_bindir} \
	MANDIR=%{_mandir}/man1 \
	RASMOLDIR=%{_libdir}/rasmol

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc PROJECTS TODO README ChangeLog doc/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_mandir}/man1/*
%{_libdir}/rasmol

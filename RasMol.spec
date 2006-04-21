# NOTE: new version at ftp://ftp.bernstein-plus-sons.com/software/RasMol_2.7.3.tar.gz
Summary:	Molecular graphics visualisation tool
Summary(pl):	Program do graficznej wizualizacji molekuЁ
Summary(ru):	Инструмент для визуализации молекулярных структур
Summary(uk):	╤нструмент для в╕зуал╕зац╕╖ молекулярних структур
Name:		RasMol2
Version:	2.6.4
Release:	1
License:	distributable
Group:		X11/Applications
Source0:	ftp://ftp.dcs.ed.ac.uk/pub/rasmol/%{name}.tar.gz
# Source0-md5:	cada76c4453f8981f0ba324a26ad1fa8
URL:		http://www.rasmol.org/
BuildRequires:	XFree86-devel
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

%description -l pl
RasMol2 to program do grafiki molekularnej maj╠cy sЁu©yФ do
wizualizacji biaЁek, kwasСw nukleinowych i maЁych cz╠steczek. Celem
programu jest wy╤wietlanie, nauka i generowanie obrazkСw o jako╤ci
nadaj╠cej siЙ do publikacji. RasMol dziaЁa na systemach Microsoft
Windows, Apple Macintosh, UNIX i VMS. Syystemy UNIX i VMS wymagaj╠ 8,
24 lub 32-bitowego ekranu systemu X Window (w wersji X11R4 lub
nowszej). Program czyta plik wspСЁrzЙdnych cz╠steczek i interaktywnie
wy╤wietla cz╠steczkЙ na ekranie w rС©nych schematach kolorСw i
reprezentacji. Aktualnie dostЙpne reprezentacje obejmuj╠ model drutowy
odtwarzaj╠cy gЁЙboko╤Ф, cylindryczne paЁ╠ki (Dreiding), sfery
wypeЁniaj╠ce przestrzeЯ (CPK), kulki i paЁ╠ki, bryЁy i splecione
wstЙgi biomolekularne, etykiety atomСw i kropkowane powierzchnie.

%description -l ru
RasMol - программа молекулярной графики, используемая для визуализации
протеинов, нуклеиновых кислот и небольших молекул. Пригодна для
отображения, обучения и генерации изображений для публикаций.

%description -l uk
RasMol - програма молекулярно╖ граф╕ки, що застосову╓ться для
в╕зуал╕зац╕╖ проте╖н╕в, нукле╖нових кислот та невеликих молекул.
Придатна до в╕дображення, навчання та генерац╕╖ зображень для
публ╕кац╕й.

%prep
%setup -q -n %{name}

%build
xmkmf
%{__make} \
	CDEBUGFLAGS="%{rpmcflags}" \
	RASMOLDIR=%{_libdir}/rasmol

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1

%{__make} install install.man \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=%{_bindir} \
	MANDIR=%{_mandir}/man1 \
	RASMOLDIR=%{_libdir}/rasmol

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc PROJECTS TODO README Announce ChangeLog doc/{*.ps,rasmol.txt}
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_mandir}/man1/*
%{_libdir}/rasmol

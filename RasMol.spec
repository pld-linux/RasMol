Summary:	Molecular graphics visualisation tool
Summary(pl):	Program do graficznej wizualizacji moleku³
Name:		RasMol2
Version:	2.6.4
Release:	1
License:	distributable
Group:		X11/Applications
Source0:	ftp://ftp.dcs.ed.ac.uk/pub/rasmol/%{name}.tar.gz
# Source0-md5:	cada76c4453f8981f0ba324a26ad1fa8
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		/usr/X11R6/man

%description
RasMol2 is a molecular graphics program intended for the visualisation
of proteins, nucleic acids and small molecules. The program is aimed
at display, teaching and generation of publication quality images.
RasMol runs on Microsoft Windows, Apple Macintosh, UNIX and VMS
systems. The UNIX and VMS systems require an 8, 24 or 32 bit colour X
Windows display (X11R4 or later). The program reads in a molecule
co-ordinate file and interactively displays the molecule on the screen
in a variety of colour schemes and molecule representations. Currently
available representations include depth-cued wireframes, 'Dreiding'
sticks, spacefilling (CPK) spheres, ball and stick, solid and strand
biomolecular ribbons, atom labels and dot surfaces.

#%description -l pl

%prep
%setup -q -n RasMol2

%build
xmkmf
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install doc/rasmol.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc PROJECTS TODO README Announce ChangeLog doc/{*.ps,rasmol.txt}
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_mandir}/man1/*
%{_libdir}/rasmol

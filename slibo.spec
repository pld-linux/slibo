Summary:	KDE chess board interface
Summary(pl.UTF-8):	Interfejs do szachownicy dla KDE
Name:		slibo
Version:	0.4.4
Release:	0.1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/slibo/%{name}-%{version}.tar.bz2
# Source0-md5:	145a2bcf3d1e9769ccd30b8f1d1ee8ea
URL:		http://slibo.sourceforge.net/
BuildRequires:	kdelibs-devel
BuildRequires:	ncurses-devel
BuildRequires:	sqlite-devel
#Suggests:	Sjeng-Free
Suggests:	crafty
Suggests:	gnuchess
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Slibo aims to be a comfortable chess interface for KDE. Designed to be
usable as a replacement for the xboard chess interface, it has much
more functionality, and, on the other hand, is easy to use. Slibo can
be used with common chess engines like crafty or gnuchess, but it
provides its own chess engine too. You can:
* Play against different engines, or watch them playing.
* Use multiple engines at the same time, for instance to analyze a
  game with different engines.
* Analyze your PGN files.
* Customize the look of the pieces and the board.

%description -l pl.UTF-8
Slibo to program tworzony jako wygodny interfejs szachowy dla KDE.
Jest zaprojektowany w celu używania jako zamiennik interfejsu xboard,
ma o wiele większą funkcjonalność, a ponadto jest łatwy w użyciu. Może
być używany z popularnymi silnikami szachowymi, takimi jak crafty czy
gnuchess, ale zawiera także własny silnik. Przy użyciu Slibo można:
- grać przeciwko różnym silnikom lub oglądać ich grę,
- używać różnych silników w tym samym czasie, na przykład do analizy
  gry z różnymi silnikami,
- analizować własne pliki PGN,
- zmieniać wygląd figur i szachownicy.

%prep
%setup -q

%build
%configure \
	CFLAGS="%{rpmcflags} `/usr/bin/ncurses5-config --cflags`"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO Documentation/*.txt
#%attr(755,root,root) %{_bindir}/*
#%{_datadir}/%{name}
#%{_desktopdir}/%{name}.desktop
#%{_mandir}/man[16]/*
#%{_pixmapsdir}/%{name}.xpm

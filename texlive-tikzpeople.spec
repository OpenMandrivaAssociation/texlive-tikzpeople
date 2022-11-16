Name:		texlive-tikzpeople
Version:	43978
Release:	1
Summary:	Draw people-shaped nodes in TikZ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tikzpeople
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzpeople.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzpeople.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides people-shaped nodes in the style of
Microsoft Visio clip art, to be used with TikZ. The available,
highly customizable, node shapes are: alice, bob, bride,
builder, businessman, charlie, chef, conductor, cowboy,
criminal, dave, devil, duck, graduate, groom, guard, jester,
judge, maininblack, mexican, nun, nurse, physician, pilot,
police, priest, sailor, santa, surgeon.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/tikzpeople
%doc %{_texmfdistdir}/doc/latex/tikzpeople

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

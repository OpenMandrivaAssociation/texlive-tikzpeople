%global tl_name tikzpeople
%global tl_revision 67840

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.4
Release:	%{tl_revision}.1
Summary:	Draw people-shaped nodes in TikZ
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/tikzpeople
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzpeople.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzpeople.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides people-shaped nodes in the style of Microsoft
Visio clip art, to be used with TikZ. The available, highly
customizable, node shapes are: alice, bob, bride, builder, businessman,
charlie, chef, conductor, cowboy, criminal, dave, devil, duck, graduate,
groom, guard, jester, judge, maininblack, mexican, nun, nurse,
physician, pilot, police, priest, sailor, santa, surgeon.


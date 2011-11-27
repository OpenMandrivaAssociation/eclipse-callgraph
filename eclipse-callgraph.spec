%global src_repo_tag   R0_6_1
%global eclipse_base   %{_libdir}/eclipse
%global install_loc    %{_libdir}/eclipse/dropins/callgraph
%global debug_package %{nil}

Name:           eclipse-callgraph
Version:        0.6.1
Release:        4
Summary:        C/C++ Call Graph Visualization Tool

Group:          Development/Java
License:        EPL
URL:            http://eclipse.org/linuxtools
# sh %{name}-fetch-src.sh
Source0:        %{name}-fetched-src-%{src_repo_tag}.tar.bz2
Source1:        %{name}-fetch-src.sh
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
ExcludeArch:    ppc64

BuildRequires: eclipse-cdt >= 6.0
BuildRequires: eclipse-gef >= 3.5.2
BuildRequires: eclipse-pde >= 3.5.2
BuildRequires: eclipse-linuxprofilingframework >= 0.5.0
Requires: systemtap >= 1.2
Requires: eclipse-gef >= 3.5.2
Requires: eclipse-cdt >= 6.0
Requires: eclipse-linuxprofilingframework >= 0.5.0

%description
Graphically displays the call hierarchy from executing a C/C++ binary, along
with various other runtime statistics.

%prep
%setup -q -n %{name}-fetched-src-%{src_repo_tag}

%build
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.linuxtools.callgraph \
 -d "cdt gef linuxprofilingframework"

%install
#installs to /usr/lib/eclipse/callgraph due to dependency on eclipse-
#linuxprofilingframework, which depends on architecture.
%{__rm} -rf %{buildroot}
install -d -m 755 %{buildroot}%{install_loc}

%{__unzip} -q -d %{buildroot}%{install_loc} \
     build/rpmBuild/org.eclipse.linuxtools.callgraph.zip 

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{install_loc}
%doc org.eclipse.linuxtools.callgraph-feature/epl-v10.html


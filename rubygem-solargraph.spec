# Generated from solargraph-0.45.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name solargraph

Name: rubygem-%{gem_name}
Version: 0.45.0
Release: 1%{?dist}
Summary: A Ruby language server
License: MIT
URL: http://solargraph.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.4
# BuildRequires: rubygem(pry)
# BuildRequires: rubygem(public_suffix) >= 3.1
# BuildRequires: rubygem(public_suffix) < 4
# BuildRequires: rubygem(rspec) >= 3.5
# BuildRequires: rubygem(rspec) < 4
# BuildRequires: rubygem(rspec) >= 3.5.0
# BuildRequires: rubygem(simplecov) >= 0.14
# BuildRequires: rubygem(simplecov) < 1
# BuildRequires: rubygem(webmock) >= 3.6
# BuildRequires: rubygem(webmock) < 4
BuildArch: noarch

%description
IDE tools for code completion, inline documentation, and static analysis.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check
pushd .%{gem_instdir}
# rspec spec
popd

%files
%dir %{gem_instdir}
%{_bindir}/solargraph
%{gem_instdir}/.github
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.travis.yml
%exclude %{gem_instdir}/.yardopts
%license %{gem_instdir}/LICENSE
%{gem_instdir}/SPONSORS.md
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%exclude %{gem_instdir}/.rspec
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/solargraph.gemspec
%doc %{gem_instdir}/yardoc

%changelog
* Tue Aug 09 2022 Pavel Valena <pvalena@redhat.com> - 0.45.0-1
- Initial package

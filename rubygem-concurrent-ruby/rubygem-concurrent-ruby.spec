%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name concurrent-ruby

Summary: Modern concurrency tools for Ruby
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.0.1
Release: 1%{?foremandist}%{?dist}
Epoch: 1
Group: Development/Languages

License: MIT
URL: https://github.com/ruby-concurrency/concurrent-ruby
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}ruby

%if 0%{?el6} && 0%{!?scl:1}
Requires: %{?scl_prefix_ruby}ruby(abi)
BuildRequires: %{?scl_prefix_ruby}ruby(abi)
%else
Requires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
%endif

BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch

Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Modern concurrency tools including agents, futures,
promises, thread pools, actors, supervisors, and more. Inspired by
Erlang, Clojure, Go, JavaScript, actors, and classic concurrency
patterns.


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{epoch}:%{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}


%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            -V --force %{SOURCE0}
%{?scl:"}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/LICENSE.txt
%{gem_libdir}

%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_docdir}

%changelog
* Mon Feb 29 2016 Dominic Cleal <dominic@cleal.org> 1.0.1-1
- Update concurrent-ruby to 1.0.1 (dominic@cleal.org)

* Tue Jan 05 2016 Dominic Cleal <dcleal@redhat.com> 1.0.0-2
- Add foremandist to plugin dependencies (dcleal@redhat.com)

* Thu Dec 24 2015 Dominic Cleal <dcleal@redhat.com> 1.0.0-1
- Update concurrent-ruby to 1.0.0 (stbenjam@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 0.9.0-5
- Fix checks against scl name, optimise rhel/empty SCL conditional
  (dcleal@redhat.com)
- Converted to tfm SCL (dcleal@redhat.com)

* Thu Aug 20 2015 Dominic Cleal <dcleal@redhat.com> 0.9.0-4
- Package concurrent-ruby for non-SCL el7 (stbenjam@redhat.com)

* Thu Aug 06 2015 Dominic Cleal <dcleal@redhat.com> 0.9.0-3
- Fix dep to include epoch between -doc and main package (dcleal@redhat.com)

* Wed Aug 05 2015 Dominic Cleal <dcleal@redhat.com> 0.9.0-2
- Increase the epoch number for the concurrent-ruby gems (inecas@redhat.com)

* Mon Aug 03 2015 Ivan Nečas <inecas@redhat.com> 0.9.0-1
- Update concurrent-ruby to 0.9.0 (inecas@redhat.com)
- Automatic commit of package [rubygem-concurrent-ruby] minor release
  [0.9.0.pre3-1]. (dcleal@redhat.com)
- Initial build of concurrent-ruby library (inecas@redhat.com)

* Thu Jul 02 2015 Ivan Nečas <inecas@redhat.com>
- new package built with tito

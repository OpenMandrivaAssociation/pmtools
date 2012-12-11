Summary:	Tools for examining kernel ACPI tables	
Name:		pmtools
Version:	20071116
Release:	%mkrel 7
License:	GPLv2
Group:		Development/Kernel		
Source:		http://www.lesswatts.org/patches/linux_acpi//%{name}-%{version}.tar.bz2	
Url:		http://www.lesswatts.org
BuildRoot:	%_tmppath/%name-%version-root

%description
This is a small collection of power management test and
investigation tools.  See http://acpi.sourceforge.net
for more information on ACPI for Linux.

%prep
%setup -q

%build
%make
%make -C madt

%install
mv madt/README madt/README.madt
install -d %buildroot%{_sbindir}
install madt/madt %buildroot%{_sbindir}
install acpidump/acpidump %buildroot%{_sbindir}
install acpixtract/acpixtract %buildroot%{_sbindir}

%clean
rm -fr %buildroot

%files
%defattr(-,root,root)
%doc README COPYING madt/README.madt madt/example.APIC.dat madt/example.APIC.bad.dat
%{_sbindir}/madt
%{_sbindir}/acpidump
%{_sbindir}/acpixtract


%changelog
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 20071116-7mdv2011.0
+ Revision: 614592
- the mass rebuild of 2010.1 packages

* Thu Feb 11 2010 Sandro Cazzaniga <kharec@mandriva.org> 20071116-6mdv2010.1
+ Revision: 504057
- Fix licence

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 20071116-5mdv2010.0
+ Revision: 430747
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 20071116-4mdv2009.0
+ Revision: 259112
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 20071116-3mdv2009.0
+ Revision: 247037
- rebuild

* Tue Feb 19 2008 Erwan Velu <erwan@mandriva.org> 20071116-1mdv2008.1
+ Revision: 173048
- Removing files that doesn't exist anymore
- New release 20071116

  + Thierry Vignaud <tv@mandriva.org>
    - fix spacing at top of description

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 20061130-1mdv2008.1
+ Revision: 125464
- kill re-definition of %%buildroot on Pixel's request


* Mon Feb 12 2007 Stew Benedict <sbenedict@mandriva.com> 20061130-1mdv2007.0
+ Revision: 120161
- Import pmtools

* Mon Feb 12 2007 Stew Benedict <sbenedict@mandriva.com> 20061130-1mdv2007.1
- 20061130

* Tue Jan 03 2006 Erwan Velu <erwan@seanodes.com>  20050926-1mdk
- 20050926

* Wed Nov 09 2005 Stew Benedict <sbenedict@mandrakesoft.com>  20050804-1mdk
- 20050804, some name changes

* Sat Oct 02 2004 Stew Benedict <sbenedict@mandrakesoft.com>  20031210-1mdk
- First mandrakelinux release


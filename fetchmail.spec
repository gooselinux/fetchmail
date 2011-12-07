%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%define fetchmailconf 0

Summary: A remote mail retrieval and forwarding utility
Name: fetchmail
Version: 6.3.17
Release: 1%{?dist}
Requires: procmail
Source0: http://download.berlios.de/fetchmail/fetchmail-%{version}.tar.xz
Source1: http://download.berlios.de/fetchmail/fetchmail-%{version}.tar.xz.asc
URL: http://fetchmail.berlios.de/
# For a breakdown of the licensing, see COPYING
License: GPL+ and Public Domain
Group: Applications/Internet
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: gettext-devel hesiod-devel krb5-devel openssl-devel procmail
%if ! %{fetchmailconf}
Obsoletes: fetchmailconf
%endif

%package -n fetchmailconf
Summary: A GUI utility for configuring your fetchmail preferences.
Group: Applications/Internet
Requires: python, tk, tkinter, fetchmail = %{version}-%{release}

%description
Fetchmail is a remote mail retrieval and forwarding utility intended
for use over on-demand TCP/IP links, like SLIP or PPP connections.
Fetchmail supports every remote-mail protocol currently in use on the
Internet (POP2, POP3, RPOP, APOP, KPOP, all IMAPs, ESMTP ETRN, IPv6,
and IPSEC) for retrieval. Then Fetchmail forwards the mail through
SMTP so you can read it through your favorite mail client.

Install fetchmail if you need to retrieve mail over SLIP or PPP
connections.

%description -n fetchmailconf
Fetchmailconf is a Tcl/Tk GUI application that edits your .fetchmailrc
file in order to configure the fetchmail mail retrieval
program. Fetchmail's numerous options may be confusing to new users,
so fetchmailconf may help to clear up the confusion.

Install fetchmailconf if you need help configuring fetchmail. You'll
need to have Python and Tk installed in order to use fetchmailconf.

%prep
%setup -q

%build
%configure --enable-POP3 --enable-IMAP --with-ssl --with-hesiod \
	--enable-ETRN --enable-NTLM --enable-SDPS --enable-RPA \
	--enable-nls --with-kerberos5 --with-gssapi \
	--enable-fallback=procmail
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%if ! %{fetchmailconf}
rm -f $RPM_BUILD_ROOT%{_bindir}/fetchmailconf*
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/fetchmailconf.1*
rm -f $RPM_BUILD_ROOT%{python_sitelib}/fetchmailconf.py*
%endif

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc COPYING FAQ FEATURES NEWS NOTES README README.SSL TODO
%{_bindir}/fetchmail
%{_mandir}/man1/fetchmail.1*

%if %{fetchmailconf}
%files -n fetchmailconf
%defattr(-,root,root)
%{_bindir}/fetchmailconf
%{python_sitelib}/fetchmailconf.py*
%{_mandir}/man1/fetchmailconf.1*
%endif

%changelog
* Wed May 12 2010 Vitezslav Crhonek <vcrhonek@redhat.com> - 6.3.17-1
- Update to fetchmail-6.3.17

* Tue Feb  9 2010 Vitezslav Crhonek <vcrhonek@redhat.com> - 6.3.11-4
- Fix CVE-2010-0562

* Mon Nov 23 2009 Dennis Gregorovic <dgregor@redhat.com> - 6.3.11-3.1
- Rebuilt for RHEL 6

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 6.3.11-3
- rebuilt with new openssl

* Tue Aug 18 2009 Vitezslav Crhonek <vcrhonek@redhat.com> - 6.3.11-2
- Regression bug fix for fetchmail 6.3.11

* Thu Aug  6 2009 Vitezslav Crhonek <vcrhonek@redhat.com> - 6.3.11-1
- Update to fetchmail-6.3.11
- Remove addrconf patch (upstream now)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.3.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 09 2009 Adam Jackson <ajax@redhat.com> 6.3.9-4
- Rebuild to get rid of libkrb4 dependency.

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.3.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 16 2009 Tomas Mraz <tmraz@redhat.com> - 6.3.9-2
- rebuild with new openssl

* Wed Dec  3 2008 Vitezslav Crhonek <vcrhonek@redhat.com> - 6.3.9-1
- Update to fetchmail-6.3.9

* Tue Sep 18 2008 Vitezslav Crhonek <vcrhonek@redhat.com> - 6.3.8-8
- Rediff all patches to work with patch --fuzz=0
- Replace server(smtp) requires by procmail
  Resolves: #66396

* Fri Jun 27 2008 Vitezslav Crhonek <vcrhonek@redhat.com> - 6.3.8-7
- Fix CVE-2008-2711

* Wed Mar 26 2008 Vitezslav Crhonek <vcrhonek@redhat.com> - 6.3.8-6
- Replace smtpdaemon requires by server(smtp) requires
  Resolves: #66396

* Mon Feb 11 2008 Vitezslav Crhonek <vcrhonek@redhat.com> - 6.3.8-5
- Fix Buildroot

* Wed Dec  5 2007 Vitezslav Crhonek <vcrhonek@redhat.com> - 6.3.8-4
- Rebuild

* Tue Sep  4 2007 Vitezslav Crhonek <vcrhonek@redhat.com> - 6.3.8-3
- Fix CVE-2007-4565

* Thu Aug 23 2007 Vitezslav Crhonek <vcrhonek@redhat.com> - 6.3.8-2
- fix license
- rebuild

* Mon Jul  2 2007 Vitezslav Crhonek <vcrhonek@redhat.com> - 6.3.8-1
- Update to fetchmail-6.3.8 (#246445)

* Mon Feb 19 2007 Miloslav Trmac <mitr@redhat.com> - 6.3.7-1
- Update to fetchmail-6.3.7

* Mon Jan 22 2007 Miloslav Trmac <mitr@redhat.com> - 6.3.6-2
- Let KPOP use PASS again
  Resolves: #223661

* Sat Jan  6 2007 Miloslav Trmac <mitr@redhat.com> - 6.3.6-1
- Update to fetchmail-6.3.6 (CVE-2006-5867, CVE-2006-5974)

* Wed Nov  1 2006 Miloslav Trmac <mitr@redhat.com> - 6.3.5-1
- Update to fetchmail-6.3.5
- Fix some rpmlint warnings

* Sun Sep 24 2006 Miloslav Trmac <mitr@redhat.com> - 6.3.4-2
- Don't increase the certificate search path on each poll (#206346)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 6.3.4-1.1
- rebuild

* Mon May  1 2006 Miloslav Trmac <mitr@redhat.com> - 6.3.4-1
- Update to fetchmail-6.3.4

* Sat Apr  1 2006 Miloslav Trmac <mitr@redhat.com> - 6.3.3-3
- Fix fetchmail-6.3.3-resolv.patch

* Fri Mar 31 2006 Miloslav Trmac <mitr@redhat.com> - 6.3.3-2
- Fix some type mismatches on 64-bit architectures
- Fix checking for res_* on architectures with newer glibc ABI

* Fri Mar 31 2006 Miloslav Trmac <mitr@redhat.com> - 6.3.3-1
- Update to fetchmail-6.3.3

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 6.3.2.1-1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 6.3.2.1-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Mon Jan 30 2006 Miloslav Trmac <mitr@redhat.com> - 6.3.2.1-1
- Update to fetchmail-6.3.2.1

* Mon Jan 23 2006 Miloslav Trmac <mitr@redhat.com> - 6.3.2-1
- Update to fetchmail-6.3.2 (CVE-2006-0321)

* Tue Dec 20 2005 Miloslav Trmac <mitr@redhat.com> - 6.3.1-1
- Update to fetchmail-6.3.1 (CVE-2005-4348)

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Dec  2 2005 Miloslav Trmac <mitr@redhat.com> - 6.3.0-1
- Update to fetchmail-6.3.0
- Remove nohesiod and nokerberos conditionals

* Wed Nov 30 2005 Miloslav Trmac <mitr@redhat.com> - 6.2.9-0.1.rc10
- Update to fetchmail-6.2.9-rc10

* Wed Nov  9 2005 Miloslav Trmac <mitr@redhat.com> - 6.2.5.2-2
- Rebuild with new openssl
- Ship README.SSL, drop html documentation copies

* Fri Jul 22 2005 Miloslav Trmac <mitr@redhat.com> - 6.2.5.2-1
- Update to fetchmail-6.2.5.2

* Thu Jul 21 2005 Miloslav Trmac <mitr@redhat.com> - 6.2.5.1-1
- Update to fetchmail-6.2.5.1 to fix CAN-2005-2335 (#163819)
- Fix crash on empty Message-ID

* Mon Jul 18 2005 Karsten Hopp <karsten@redhat.de> 6.2.5-10
- Buildrequires gettext-devel for AM_GNU_GETTEXT macro

* Sat Jun 11 2005 Miloslav Trmac <mitr@redhat.com> - 6.2.5-9
- Fix fetchmailconf handling of unspecified server port

* Tue Jun  7 2005 Miloslav Trmac <mitr@redhat.com> - 6.2.5-8
- Fix APOP and RPOP (#127315)
- Don't link to libdl

* Wed Mar 16 2005 Nalin Dahyabhai <nalin@redhat.com> 6.2.5-7
- stop using one of the libkrb5 private functions

* Thu Sep 30 2004 John Dennis <jdennis@redhat.com> 6.2.5-6
- fix bug #113492
  after expunge, dovecot hangs fetchmail if new e-mail came in

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed May 19 2004 Nalin Dahyabhai <nalin@redhat.com> 6.2.5-4
- turn on SDPS (#123599) and RPA

* Wed May 19 2004 Joe Orton <jorton@redhat.com> 6.2.5-3
- pass AI_ADDRCONFIG to getaddrinfo to prevent pointless AAAA lookups

* Wed Apr 21 2004 Nalin Dahyabhai <nalin@redhat.com> 6.2.5-2
- distill out portions of pop3.c which don't affect capa probing

* Fri Apr 16 2004 Nalin Dahyabhai <nalin@redhat.com>
- switch to Robert Scheck's fix for capa probing endless loop on pop servers
  which don't support capa (#115474)

* Thu Apr 15 2004 Nalin Dahyabhai <nalin@redhat.com>
- split the use-correct-service-name and check-for-gssapi-in-pop portions of
  gssapi+pop fix into pieces
- only trigger pop capa probe if authentication method != password

* Mon Mar 15 2004 Nalin Dahyabhai <nalin@redhat.com> 6.2.5-1
- update to 6.2.5, per Eric's recommendation

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Feb  2 2004 Nalin Dahyabhai <nalin@redhat.com> 6.2.0-9
- add patch to ensure that stuffed warnings always end in cr-lf (#114470)

* Tue Nov 25 2003 Nalin Dahyabhai <nalin@redhat.com>
- blah, merge multiple patches for krb5-config things into one

* Fri Nov 14 2003 Nalin Dahyabhai <nalin@redhat.com>
- fix gssapi support authenticating to imap, even when connected to pop

* Thu Nov 13 2003 Nalin Dahyabhai <nalin@redhat.com>
- munge, munge, munge.  kpop build resurrected, at least for now.

* Fri Oct 10 2003 Nalin Dahyabhai <nalin@redhat.com> 6.2.0-8
- add patch to not truncate headers which have been munged to include a
  hostname where one didn't exist before (CAN-2003-0792), backport from fix
  for 6.2.4 included in 6.2.5

* Thu Oct  9 2003 Nalin Dahyabhai <nalin@redhat.com>
- add patch from Markus Friedl to fix possible buffer underrun (CAN-2003-0790)

* Tue Sep 23 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- allow compiling without hesiod

* Tue Jun 22 2003 Nalin Dahyabhai <nalin@redhat.com> 6.2.0-6
- rebuild

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Apr 29 2003 Nalin Dahyabhai <nalin@redhat.com>
- update URLs

* Wed Jan 22 2003 Tim Powers <timp@redhat.com> 6.2.0-3
- rebuilt

* Tue Jan  7 2003 Nalin Dahyabhai <nalin@redhat.com> 6.2.0-2
- rebuild

* Fri Dec 13 2002 Nalin Dahyabhai <nalin@redhat.com> 6.2.0-1
- update to 6.2.0

* Mon Nov  4 2002 Nalin Dahyabhai <nalin@redhat.com> 6.1.2-1
- update to 6.1.2

* Fri Oct  4 2002 Nalin Dahyabhai <nalin@redhat.com> 6.1.0-1
- add -L/usr/kerberos/%%{_lib} to LDFLAGS so that the Kerberos libraries will
  be found again

* Wed Sep 25 2002 Nalin Dahyabhai <nalin@redhat.com>
- update to 6.0.0

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Jun 11 2002 Nalin Dahyabhai <nalin@redhat.com> 5.9.0-15
- remove and obsolete the fetchmailconf subpackage (tkinter is gone, so it
  can't be run)

* Mon Jun  3 2002 Nalin Dahyabhai <nalin@redhat.com> 5.9.0-14
- require hesiod at build-time

* Sun May 26 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri May 17 2002 Nalin Dahyabhai <nalin@redhat.com> 5.9.0-12
- rebuild in new environment
- require autoconf213
- enable hesiod support

* Wed May  1 2002 Nalin Dahyabhai <nalin@redhat.com> 5.9.0-11
- rebuild

* Wed May  1 2002 Nalin Dahyabhai <nalin@redhat.com> 5.9.0-10
- reject bogusly large message counts on 64-bit systems, too

* Wed Mar 27 2002 Nalin Dahyabhai <nalin@redhat.com> 5.9.0-8
- configure with --enable-NTLM, not --enable-ntlm, ditto for ETRN, POP3, IMAP

* Mon Mar 11 2002 Nalin Dahyabhai <nalin@redhat.com>
- add patch to reject bogusly large message counts, backported from 5.9.10
- build for RHL 6.2 errata

* Fri Feb 22 2002 Nalin Dahyabhai <nalin@redhat.com> 5.9.0-5
- rebuild

* Wed Jan 23 2002 Nalin Dahyabhai <nalin@redhat.com> 5.9.0-4
- rebuild in new environment

* Wed Jan 09 2002 Tim Powers <timp@redhat.com> 5.9.0-3
- automated rebuild

* Tue Nov 13 2001 Nalin Dahyabhai <nalin@redhat.com> 5.9.0-2
- remove explicit dependency on krb5-libs

* Mon Aug 13 2001 Nalin Dahyabhai <nalin@redhat.com> 5.9.0-1
- update to 5.9.0 final release

* Thu Aug  9 2001 Nalin Dahyabhai <nalin@redhat.com>
- update to 5.8.17, candidate for 5.9.0

* Tue Jul 17 2001 Nalin Dahyabhai <nalin@redhat.com>
- update to 5.8.14

* Fri Jul  6 2001 Nalin Dahyabhai <nalin@redhat.com>
- update to 5.8.12

* Mon Jul  2 2001 Nalin Dahyabhai <nalin@redhat.com>
- update to 5.8.11

* Mon Jun 25 2001 Nalin Dahyabhai <nalin@redhat.com>
- fetchmailconf should depend on tkinter (#42156)

* Thu Jun 21 2001 Nalin Dahyabhai <nalin@redhat.com>
- update to 5.8.8

* Tue Jun 19 2001 Nalin Dahyabhai <nalin@redhat.com>
- update to 5.8.7

* Tue Jun 12 2001 Nalin Dahyabhai <nalin@redhat.com>
- update to 5.8.6, which approaches a 5.9.0

* Wed May 30 2001 Nalin Dahyabhai <nalin@redhat.com>
- update to 5.8.5

* Tue May 22 2001 Nalin Dahyabhai <nalin@redhat.com>
- update to 5.8.4

* Fri Apr 27 2001 Nalin Dahyabhai <nalin@redhat.com>
- rebuild in new environment

* Tue Apr 17 2001 Nalin Dahyabhai <nalin@redhat.com>
- update to 5.8.1, which includes patches we were using

* Wed Apr  4 2001 Nalin Dahyabhai <nalin@redhat.com>
- fix handling of "any" authentication (#32527)
- accept more arguments to --auth
- parse "auth password" correctly in the configuration file

* Wed Mar 21 2001 Nalin Dahyabhai <nalin@redhat.com>
- fall back to plain auth if gssapi fails (#32527)

* Tue Mar 13 2001 Nalin Dahyabhai <nalin@redhat.com>
- properly handle "nospambounce" in the config file (#31234)

* Mon Mar 12 2001 Nalin Dahyabhai <nalin@redhat.com>
- update to 5.7.4, which merges our patches

* Mon Mar  5 2001 Nalin Dahyabhai <nalin@redhat.com>
- update to 5.7.2
- call AC_PROG_MAKE_SET in configure.in
- fix various things which cause it to not compile if gssapi is enabled

* Fri Mar  2 2001 Nalin Dahyabhai <nalin@redhat.com>
- rebuild in new environment

* Fri Feb 23 2001 Trond Eivind Glomsrød <teg@redhat.com>
- langify

* Mon Feb 12 2001 Nalin Dahyabhai <nalin@redhat.com>
- work around sockets without an sa_len field

* Fri Feb  9 2001 Nalin Dahyabhai <nalin@redhat.com>
- fix for exception when adding hosts in fetchmailconf (#26387)

* Thu Feb  8 2001 Nalin Dahyabhai <nalin@redhat.com>
- add Todd Sabin's patch for handling untagged responses during CRAM-MD5 auth

* Mon Jan 15 2001 Nalin Dahyabhai <nalin@redhat.com>
- enable IPv6 support (#24033)

* Tue Nov 28 2000 Nalin Dahyabhai <nalin@redhat.com>
- enable NLS (#21419)

* Mon Nov 27 2000 Nalin Dahyabhai <nalin@redhat.com>
- update to 5.6.0
- revert "untagged" patch, which went upstream

* Wed Nov  8 2000 Nalin Dahyabhai <nalin@redhat.com>
- patch to handle untagged responses during IMAP-GSS authentication
- update to 5.5.5

* Thu Aug 17 2000 Nalin Dahyabhai <nalin@redhat.com>
- enable SSL support

* Sat Aug 12 2000 Nalin Dahyabhai <nalin@redhat.com>
- update to 5.5.0
- change Copyright: to License: GPL

* Tue Aug  8 2000 Nalin Dahyabhai <nalin@redhat.com>
- back out MDA patch; sendmail started listening by default again

* Thu Aug  3 2000 Nalin Dahyabhai <nalin@redhat.com>
- patch to use procmail as an MDA by default
- patch to not run makedepend

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Sun Jul  2 2000 Nalin Dahyabhai <nalin@redhat.com>
- update to 5.4.3

* Thu Jun 29 2000 Nalin Dahyabhai <nalin@redhat.com>
- fix a typo in 5.4.2

* Wed Jun 28 2000 Matt Wilson <msw@redhat.com>
- fixed configure arguments to not have a continuation at the end of the last
  one

* Tue Jun 27 2000 Nalin Dahyabhai <nalin@redhat.com>
- update to 5.4.2

* Fri Jun  9 2000 Nalin Dahyabhai <nalin@redhat.com>
- update to 5.4.1
- FHS fixes, with mandir override
- change fetchmailconf.1 symlink to an include

* Thu May 25 2000 Nalin Dahyabhai <nalin@redhat.com>
- fix Kerberos configure patch to work correctly for krb5 1.0, too

* Fri May 19 2000 Nalin Dahyabhai <nalin@redhat.com>
- update to 5.4.0
- rework Kerberos dependencies

* Fri Apr 21 2000 Nalin Dahyabhai <nalin@redhat.com>
- update to 5.3.8

* Tue Apr  4 2000 Bill Nottingham <notting@redhat.com>
- eliminate explicit krb5-configs dependency

* Mon Mar  6 2000 Bernhard Rosenkränzer <bero@redhat.com>
- 5.3.1 - This fixes Bugs #9982 and #9987

* Wed Mar  1 2000 Nalin Dahyabhai <nalin@redhat.com>
- make kerberos support conditional at build-time

* Wed Mar  1 2000 Bill Nottingham <notting@redhat.com>
- integrate kerberos support into main tree

* Fri Feb 25 2000 Nalin Dahyabhai <nalin@redhat.com>
- Add Kerberos and GSS authenticator support

* Fri Feb 25 2000 Cristian Gafton <gafton@redhat.com>
- version 5.3.0 has a correct version of the rfc822 patch

* Fri Feb 25 2000 Jeff Johnson <jbj@redhat.com>
- fix length of rfc822 headers in strcncasecmp().

* Tue Feb 15 2000 Bernhard Rosenkränzer <bero@redhat.com>
- 5.2.8 (fixes the POP3-UIDL bug)
- Fix up the fetchmailconf man page symlink

* Fri Feb 11 2000 Cristian Gafton <gafton@redhat.com>
- version 5.2.7
- add patch so that fetchmailconf will not output ssl configure statements
  is no ssl is configured

* Mon Jan 31 2000 Cristian Gafton <gafton@redhat.com>
- rebuild to fix deps
- man pages are compressed
- enable %%clean

* Tue Jan 11 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 5.2.3
- fetchmailconf requires fetchmail = %%{version}
- fix compilation

* Mon Dec 27 1999 Bernhard Rosenkraenzer <bero@redhat.com>
- 5.2.2

* Thu Sep 23 1999 Preston Brown <pbrown@redhat.com>
- got 5.1.0, fixes potential buffer overflow...

* Sat Jun 12 1999 Jeff Johnson <jbj@redhat.com>
- update to 5.0.4.

* Mon Apr 05 1999 Cristian Gafton <gafton@redhat.com>
- 5.0.0

* Tue Mar 30 1999 Preston Brown <pbrown@redhat.com>
- subpackage for fetchmailconf

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 2)

* Thu Dec 17 1998 Cristian Gafton <gafton@redhat.com>
- version 4.7.0
- build against glibc 2.1

* Sat Sep 19 1998 Jeff Johnson <jbj@redhat.com>
- correct typo in dangling symlink fix.

* Wed Sep 09 1998 Cristian Gafton <gafton@redhat.com>
- update to 4.5.8

* Wed Jul 22 1998 Jeff Johnson <jbj@redhat.com>
- update to 4.5.3.

* Fri May 08 1998 Cristian Gafton <gafton@redhat.com>
- fixed spelung eror in the decsriptoin

* Thu May 07 1998 Cristian Gafton <gafton@redhat.com>
- new version 4.4.4 fixes a lot of bugs

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 09 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 4.4.1
- buildroot

* Thu Oct 23 1997 Michael Fulbright <msf@redhat.com>
- Updated to 4.3.2 using SRPM from Eric Raymond

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc

# CVE Digest Summary (2026-07-08)

- 取得日時: 2026-07-08 13:10:55 JST
- 新規掲載件数: 30
- 出力対象: 新規CVEのみ

## 緊急対応候補

### CVE-2026-31431: Linux Kernel Incorrect Resource Transfer Between Spheres Vulnerability

- 重要度: KEV
- CVSS: -
- KEV掲載: yes
- 関連キーワード: linux
- 影響製品: Linux Kernel
- 公開日: 2026-05-01
- 更新日: -
- 出典: CISA KEV
- 概要: Linux Kernel contains an incorrect resource transfer between spheres vulnerability that could allow for privilege escalation.
- 参照:
  - https://lore.kernel.org/linux-cve-announce/2026042214-CVE-2026-31431-3d65@gregkh/; https://xint.io/blog/copy-fail-linux-distributions#the-fix-6 ; https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/about/ ; https://nvd.nist.gov/vuln/detail/CVE-2026-31431

### CVE-2020-15415: DrayTek Multiple Vigor Routers OS Command Injection Vulnerability

- 重要度: KEV
- CVSS: -
- KEV掲載: yes
- 関連キーワード: python
- 影響製品: DrayTek Multiple Vigor Routers
- 公開日: 2024-09-30
- 更新日: -
- 出典: CISA KEV
- 概要: DrayTek Vigor3900, Vigor2960, and Vigor300B devices contain an OS command injection vulnerability in cgi-bin/mainfunction.cgi/cvmcfgupload that allows for remote code execution via shell metacharacters in a filename when the text/x-python-script content type is used.
- 参照:
  - https://www.draytek.com/about/security-advisory/vigor3900-/-vigor2960-/-vigor300b-remote-code-injection/execution-vulnerability-(cve-2020-14472) ; https://nvd.nist.gov/vuln/detail/CVE-2020-15415

### CVE-2025-30066: tj-actions/changed-files GitHub Action Embedded Malicious Code Vulnerability

- 重要度: KEV
- CVSS: -
- KEV掲載: yes
- 関連キーワード: npm, github actions, aws
- 影響製品: tj-actions changed-files GitHub Action
- 公開日: 2025-03-18
- 更新日: -
- 出典: CISA KEV
- 概要: tj-actions/changed-files GitHub Action contains an embedded malicious code vulnerability that allows a remote attacker to discover secrets by reading Github Actions Workflow Logs. These secrets may include, but are not limited to, valid AWS access keys, GitHub personal access tokens (PATs), npm tokens, and private RSA...
- 参照:
  - This vulnerability affects a common open-source project, third-party library, or a protocol used by different products. For more information, please see: CISA Mitigation Instructions: https://www.cisa.gov/news-events/alerts/2025/03/18/supply-chain-compromise-third-party-tj-actionschanged-files-cve-2025-30066-and-reviewdogaction ; Additional References: https://github.com/tj-actions/changed-files/blob/45fb12d7a8bedb4da42342e52fe054c6c2c3fd73/README.md?plain=1#L20-L28 ; https://nvd.nist.gov/vuln/detail/CVE-2025-30066

### CVE-2022-0492: Linux Kernel Improper Authentication Vulnerability

- 重要度: KEV
- CVSS: -
- KEV掲載: yes
- 関連キーワード: linux
- 影響製品: Linux Kernel
- 公開日: 2026-06-02
- 更新日: -
- 出典: CISA KEV
- 概要: Linux Kernel contains an improper authentication vulnerability which could allow for privilege escalation via the cgroups v1 release_agent feature.
- 参照:
  - This vulnerability affects a common open-source component, third-party library, or a protocol used by different products. Please check with specific vendors for information on patching status. For more information, please see: https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=24f6008564183aa120d07c03d9289519c2fe02af ; https://www.kernel.org/ ; https://nvd.nist.gov/vuln/detail/CVE-2022-0492

### CVE-2025-11953: React Native Community CLI OS Command Injection Vulnerability

- 重要度: KEV
- CVSS: -
- KEV掲載: yes
- 関連キーワード: react
- 影響製品: React Native Community CLI
- 公開日: 2026-02-05
- 更新日: -
- 出典: CISA KEV
- 概要: React Native Community CLI contains an OS command injection vulnerability which could allow unauthenticated network attackers to send POST requests to the Metro Development Server and run arbitrary executables via a vulnerable endpoint exposed by the server. On Windows, attackers can also execute arbitrary shell comman...
- 参照:
  - This vulnerability could affect an open-source component, third-party library, protocol, or proprietary implementation that could be used by different products. For more information, please see: https://github.com/react-native-community/cli/commit/15089907d1f1301b22c72d7f68846a2ef20df547 ; https://github.com/react-native-community/cli/pull/2735 ; https://nvd.nist.gov/vuln/detail/CVE-2025-11953

### CVE-2025-55182: Meta React Server Components Remote Code Execution Vulnerability

- 重要度: KEV
- CVSS: -
- KEV掲載: yes
- 関連キーワード: react
- 影響製品: Meta React Server Components
- 公開日: 2025-12-05
- 更新日: -
- 出典: CISA KEV
- 概要: Meta React Server Components contains a remote code execution vulnerability that could allow unauthenticated remote code execution by exploiting a flaw in how React decodes payloads sent to React Server Function endpoints. Please note CVE-2025-66478 has been rejected, but it is associated with CVE-2025- 55182.
- 参照:
  - Check for signs of potential compromise on all internet accessible REACT instances after applying mitigations. For more information, please see: https://react.dev/blog/2025/12/03/critical-security-vulnerability-in-react-server-components ; https://github.com/vercel-labs/fix-react2shell-next?tab=readme-ov-file ; https://nvd.nist.gov/vuln/detail/CVE-2025-55182

### CVE-2024-50302: Linux Kernel Use of Uninitialized Resource Vulnerability

- 重要度: KEV
- CVSS: -
- KEV掲載: yes
- 関連キーワード: linux
- 影響製品: Linux Kernel
- 公開日: 2025-03-04
- 更新日: -
- 出典: CISA KEV
- 概要: The Linux kernel contains a use of uninitialized resource vulnerability that allows an attacker to leak kernel memory via a specially crafted HID report.
- 参照:
  - This vulnerability affects a common open-source component, third-party library, or a protocol used by different products. For more information, please see: https://lore.kernel.org/linux-cve-announce/2024111908-CVE-2024-50302-f677@gregkh/ ; https://source.android.com/docs/security/bulletin/2025-03-01 ; https://nvd.nist.gov/vuln/detail/CVE-2024-50302

### CVE-2024-55591: Fortinet FortiOS and FortiProxy Authentication Bypass Vulnerability

- 重要度: KEV
- CVSS: -
- KEV掲載: yes
- 関連キーワード: node.js
- 影響製品: Fortinet FortiOS and FortiProxy
- 公開日: 2025-01-14
- 更新日: -
- 出典: CISA KEV
- 概要: Fortinet FortiOS and FortiProxy contain an authentication bypass vulnerability that may allow an unauthenticated, remote attacker to gain super-admin privileges via crafted requests to Node.js websocket module.
- 参照:
  - https://fortiguard.fortinet.com/psirt/FG-IR-24-535 ; https://nvd.nist.gov/vuln/detail/CVE-2024-55591

### CVE-2024-36971: Android Kernel Remote Code Execution Vulnerability

- 重要度: KEV
- CVSS: -
- KEV掲載: yes
- 関連キーワード: linux
- 影響製品: Android Kernel
- 公開日: 2024-08-07
- 更新日: -
- 出典: CISA KEV
- 概要: Android contains an unspecified vulnerability in the kernel that allows for remote code execution. This vulnerability resides in Linux Kernel and could impact other products, including but not limited to Android OS.
- 参照:
  - This vulnerability affects a common open-source component, third-party library, or a protocol used by different products. Please check with specific vendors for information on patching status. For more information, please see:   https://source.android.com/docs/security/bulletin/2024-08-01,  https://lore.kernel.org/linux-cve-announce/20240610090330.1347021-2-lee@kernel.org/T/#u ; https://nvd.nist.gov/vuln/detail/CVE-2024-36971

### CVE-2024-1086: Linux Kernel Use-After-Free Vulnerability

- 重要度: KEV
- CVSS: -
- KEV掲載: yes
- 関連キーワード: linux
- 影響製品: Linux Kernel
- 公開日: 2024-05-30
- 更新日: -
- 出典: CISA KEV
- 概要: Linux kernel contains a use-after-free vulnerability in the netfilter: nf_tables component that allows an attacker to achieve local privilege escalation.
- 参照:
  - This vulnerability affects a common open-source component, third-party library, or a protocol used by different products. Please check with specific vendors for information on patching status. For more information, please see: https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=f342de4e2f33e0e39165d8639387aa6c19dff660;   https://nvd.nist.gov/vuln/detail/CVE-2024-1086

### CVE-2023-28434: MinIO Security Feature Bypass Vulnerability

- 重要度: KEV
- CVSS: -
- KEV掲載: yes
- 関連キーワード: aws
- 影響製品: MinIO MinIO
- 公開日: 2023-09-19
- 更新日: -
- 出典: CISA KEV
- 概要: MinIO contains a security feature bypass vulnerability that allows an attacker to use crafted requests to bypass metadata bucket name checking and put an object into any bucket while processing `PostPolicyBucket` to conduct privilege escalation. To carry out this attack, the attacker requires credentials with `arn:aws:...
- 参照:
  - https://github.com/minio/minio/security/advisories/GHSA-2pxw-r47w-4p8c;  https://nvd.nist.gov/vuln/detail/CVE-2023-28434

### CVE-2023-34362: Progress MOVEit Transfer SQL Injection Vulnerability

- 重要度: KEV
- CVSS: -
- KEV掲載: yes
- 関連キーワード: mysql
- 影響製品: Progress MOVEit Transfer
- 公開日: 2023-06-02
- 更新日: -
- 出典: CISA KEV
- 概要: Progress MOVEit Transfer contains a SQL injection vulnerability that could allow an unauthenticated attacker to gain unauthorized access to MOVEit Transfer's database. Depending on the database engine being used (MySQL, Microsoft SQL Server, or Azure SQL), an attacker may be able to infer information about the structur...
- 参照:
  - This CVE has a CISA AA located here: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-158a. Please see the AA for associated IOCs. Additional information is available at: https://community.progress.com/s/article/MOVEit-Transfer-Critical-Vulnerability-31May2023.;  https://nvd.nist.gov/vuln/detail/CVE-2023-34362

### CVE-2023-0266: Linux Kernel Use-After-Free Vulnerability

- 重要度: KEV
- CVSS: -
- KEV掲載: yes
- 関連キーワード: linux
- 影響製品: Linux Kernel
- 公開日: 2023-03-30
- 更新日: -
- 出典: CISA KEV
- 概要: Linux kernel contains a use-after-free vulnerability that allows for privilege escalation to gain ring0 access from the system user.
- 参照:
  - https://git.kernel.org/pub/scm/linux/kernel/git/stable/stable-queue.git/tree/queue-5.10/alsa-pcm-move-rwsem-lock-inside-snd_ctl_elem_read-to-prevent-uaf.patch?id=72783cf35e6c55bca84c4bb7b776c58152856fd4;  https://nvd.nist.gov/vuln/detail/CVE-2023-0266

### CVE-2021-3493: Linux Kernel Privilege Escalation Vulnerability

- 重要度: KEV
- CVSS: -
- KEV掲載: yes
- 関連キーワード: linux
- 影響製品: Linux Kernel
- 公開日: 2022-10-20
- 更新日: -
- 出典: CISA KEV
- 概要: The overlayfs stacking file system in Linux kernel does not properly validate the application of file capabilities against user namespaces, which could lead to privilege escalation.
- 参照:
  - https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=7c03e2cda4a584cadc398e8f6641ca9988a39d52; https://nvd.nist.gov/vuln/detail/CVE-2021-3493

### CVE-2013-6282: Linux Kernel Improper Input Validation Vulnerability

- 重要度: KEV
- CVSS: -
- KEV掲載: yes
- 関連キーワード: linux
- 影響製品: Linux Kernel
- 公開日: 2022-09-15
- 更新日: -
- 出典: CISA KEV
- 概要: The get_user and put_user API functions of the Linux kernel fail to validate the target address when being used on ARM v6k/v7 platforms. This allows an application to read and write kernel memory which could lead to privilege escalation.
- 参照:
  - https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=8404663f81d212918ff85f493649a7991209fa04; https://nvd.nist.gov/vuln/detail/CVE-2013-6282

### CVE-2013-2596: Linux Kernel Integer Overflow Vulnerability

- 重要度: KEV
- CVSS: -
- KEV掲載: yes
- 関連キーワード: linux
- 影響製品: Linux Kernel
- 公開日: 2022-09-15
- 更新日: -
- 出典: CISA KEV
- 概要: Linux kernel fb_mmap function in drivers/video/fbmem.c contains an integer overflow vulnerability that allows for privilege escalation.
- 参照:
  - https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=fc9bbca8f650e5f738af8806317c0a041a48ae4a; https://nvd.nist.gov/vuln/detail/CVE-2013-2596

### CVE-2013-2094: Linux Kernel Privilege Escalation Vulnerability

- 重要度: KEV
- CVSS: -
- KEV掲載: yes
- 関連キーワード: linux
- 影響製品: Linux Kernel
- 公開日: 2022-09-15
- 更新日: -
- 出典: CISA KEV
- 概要: Linux kernel fails to check all 64 bits of attr.config passed by user space, resulting to out-of-bounds access of the perf_swevent_enabled array in sw_perf_event_destroy(). Explotation allows for privilege escalation.
- 参照:
  - https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=8176cced706b5e5d15887584150764894e94e02f; https://nvd.nist.gov/vuln/detail/CVE-2013-2094

### CVE-2020-36193: PEAR Archive_Tar Improper Link Resolution Vulnerability

- 重要度: KEV
- CVSS: -
- KEV掲載: yes
- 関連キーワード: linux
- 影響製品: PEAR Archive_Tar
- 公開日: 2022-08-25
- 更新日: -
- 出典: CISA KEV
- 概要: PEAR Archive_Tar Tar.php allows write operations with directory traversal due to inadequate checking of symbolic links. PEAR stands for PHP Extension and Application Repository and it is an open-source framework and distribution system for reusable PHP components with known usage in third-party products such as Drupal...
- 参照:
  - https://github.com/pear/Archive_Tar/commit/cde460582ff389404b5b3ccb59374e9b389de916, https://www.drupal.org/sa-core-2021-001, https://access.redhat.com/security/cve/cve-2020-36193; https://nvd.nist.gov/vuln/detail/CVE-2020-36193

### CVE-2020-28949: PEAR Archive_Tar Deserialization of Untrusted Data Vulnerability

- 重要度: KEV
- CVSS: -
- KEV掲載: yes
- 関連キーワード: linux
- 影響製品: PEAR Archive_Tar
- 公開日: 2022-08-25
- 更新日: -
- 出典: CISA KEV
- 概要: PEAR Archive_Tar allows an unserialization attack because phar: is blocked but PHAR: is not blocked. PEAR stands for PHP Extension and Application Repository and it is an open-source framework and distribution system for reusable PHP components with known usage in third-party products such as Drupal Core and Red Hat Li...
- 参照:
  - https://pear.php.net/bugs/bug.php?id=27002, https://www.drupal.org/sa-core-2020-013, https://access.redhat.com/security/cve/cve-2020-28949; https://nvd.nist.gov/vuln/detail/CVE-2020-28949

### CVE-2021-22600: Linux Kernel Privilege Escalation Vulnerability

- 重要度: KEV
- CVSS: -
- KEV掲載: yes
- 関連キーワード: linux
- 影響製品: Linux Kernel
- 公開日: 2022-04-11
- 更新日: -
- 出典: CISA KEV
- 概要: Linux Kernel contains a flaw in the packet socket (AF_PACKET) implementation which could lead to incorrectly freeing memory. A local user could exploit this for denial-of-service (DoS) or possibly for privilege escalation.
- 参照:
  - https://nvd.nist.gov/vuln/detail/CVE-2021-22600

### CVE-2010-1871: Red Hat Linux JBoss Seam 2 Remote Code Execution Vulnerability

- 重要度: KEV
- CVSS: -
- KEV掲載: yes
- 関連キーワード: linux
- 影響製品: Red Hat JBoss Seam 2
- 公開日: 2021-12-10
- 更新日: -
- 出典: CISA KEV
- 概要: JBoss Seam 2 (jboss-seam2), as used in JBoss Enterprise Application Platform 4.3.0 for Red Hat Linux, allows attackers to perform remote code execution. This vulnerability can only be exploited when the Java Security Manager is not properly configured.
- 参照:
  - https://nvd.nist.gov/vuln/detail/CVE-2010-1871

### CVE-2019-2215: Android Kernel Use-After-Free Vulnerability

- 重要度: KEV
- CVSS: -
- KEV掲載: yes
- 関連キーワード: linux
- 影響製品: Android Android Kernel
- 公開日: 2021-11-03
- 更新日: -
- 出典: CISA KEV
- 概要: Android Kernel contains a use-after-free vulnerability in binder.c that allows for privilege escalation from an application to the Linux Kernel. This vulnerability was observed chained with CVE-2020-0041 and CVE-2020-0069 under exploit chain "AbstractEmu."
- 参照:
  - https://nvd.nist.gov/vuln/detail/CVE-2019-2215

### CVE-2020-0069: Mediatek Multiple Chipsets Insufficient Input Validation Vulnerability

- 重要度: KEV
- CVSS: -
- KEV掲載: yes
- 関連キーワード: linux
- 影響製品: MediaTek Multiple Chipsets
- 公開日: 2021-11-03
- 更新日: -
- 出典: CISA KEV
- 概要: Multiple MediaTek chipsets contain an insufficient input validation vulnerability and have missing SELinux restrictions in the Command Queue drivers ioctl handlers. This causes an out-of-bounds write leading to privilege escalation. This vulnerability was observed chained with CVE-2019-2215 and CVE-2020-0041 under expl...
- 参照:
  - https://nvd.nist.gov/vuln/detail/CVE-2020-0069

### CVE-2021-21315: System Information Library for Node.JS Command Injection

- 重要度: KEV
- CVSS: -
- KEV掲載: yes
- 関連キーワード: node.js, npm
- 影響製品: Npm package System Information Library for Node.JS
- 公開日: 2022-01-18
- 更新日: -
- 出典: CISA KEV
- 概要: In this vulnerability, an attacker can send a malicious payload that will exploit the name parameter. After successful exploitation, attackers can execute remote.
- 参照:
  - https://nvd.nist.gov/vuln/detail/CVE-2021-21315

### CVE-2026-56290: Joomlack Page Builder Improper Access Control Vulnerability

- 重要度: KEV
- CVSS: -
- KEV掲載: yes
- 関連キーワード: -
- 影響製品: Joomlack Page Builder
- 公開日: 2026-07-07
- 更新日: -
- 出典: CISA KEV
- 概要: Joomlack Page Builder contains an improper access control vulnerability that could allow for remote code execution via unauthenticated arbitrary file upload.
- 参照:
  - https://www.joomlack.fr/en/joomla-extensions/page-builder-ck ; BOD 26-04: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk ; Forensics Triage Requirements: https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk ; https://nvd.nist.gov/vuln/detail/CVE-2026-56290

### CVE-2026-20253: Splunk Enterprise Missing Authentication for Critical Function Vulnerability

- 重要度: KEV
- CVSS: -
- KEV掲載: yes
- 関連キーワード: postgresql
- 影響製品: Splunk Enterprise
- 公開日: 2026-06-18
- 更新日: -
- 出典: CISA KEV
- 概要: Splunk Enterprise contains a missing authentication for critical function vulnerability which could allow an unauthenticated user to create or truncate arbitrary files through a PostgreSQL sidecar service endpoint.
- 参照:
  - https://advisory.splunk.com/advisories/SVD-2026-0603 ; BOD 26-04: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk ; Forensics Triage Requirements: https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk ; https://nvd.nist.gov/vuln/detail/CVE-2026-20253

### CVE-2026-54420: LiteSpeed cPanel Plugin UNIX Symbolic Link (Symlink) Following Vulnerability

- 重要度: KEV
- CVSS: -
- KEV掲載: yes
- 関連キーワード: linux
- 影響製品: LiteSpeed cPanel Plugin
- 公開日: 2026-06-15
- 更新日: -
- 出典: CISA KEV
- 概要: LiteSpeed cPanel plugin contains a UNIX symbolic link (Symlink) following vulnerability that could allow a user with FTP or web shell access on a shared hosting server running CloudLinux/CageFS.
- 参照:
  - https://blog.litespeedtech.com/2026/06/01/security-update-for-litespeed-cpanel-plugin-2/ ; BOD 26-04: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk ; Forensics Triage Requirements: https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk ; https://nvd.nist.gov/vuln/detail/CVE-2026-54420

### CVE-2026-45321: TanStack Unspecified Vulnerability

- 重要度: KEV
- CVSS: -
- KEV掲載: yes
- 関連キーワード: npm
- 影響製品: TanStack TanStack
- 公開日: 2026-05-27
- 更新日: -
- 出典: CISA KEV
- 概要: TanStack contains an unspecified vulnerability that allowed malicious versions of the product to be published to the npm registry to publish credential-stealing malware under a trusted identity.
- 参照:
  - This vulnerability could affect an open-source component, third-party library, protocol, or proprietary implementation that could be used by different products. For more information, please see: https://github.com/TanStack/router/security/advisories/GHSA-g7cv-rxg3-hmpx ; https://nvd.nist.gov/vuln/detail/CVE-2026-45321

### CVE-2018-14634: Linux Kernel Integer Overflow Vulnerability

- 重要度: KEV
- CVSS: -
- KEV掲載: yes
- 関連キーワード: linux
- 影響製品: Linux Kernel
- 公開日: 2026-01-26
- 更新日: -
- 出典: CISA KEV
- 概要: Linux Kernel contains an integer overflow vulnerability in the create_elf_tables() function which could allow an unprivileged local user with access to SUID (or otherwise privileged) binary to escalate their privileges on the system.
- 参照:
  - This vulnerability affects a common open-source component, third-party library, or a protocol used by different products. Please check with specific vendors for information on patching status. For more information, please see: https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/about/ ; https://www.kernel.org/ ; https://www.cve.org/CVERecord?id=CVE-2018-14634 ; https://access.redhat.com/errata/RHSA-2018:3540 ; https://nvd.nist.gov/vuln/detail/CVE-2018-14634

### CVE-2021-22555: Linux Kernel Heap Out-of-Bounds Write Vulnerability

- 重要度: KEV
- CVSS: -
- KEV掲載: yes
- 関連キーワード: linux
- 影響製品: Linux Kernel
- 公開日: 2025-10-06
- 更新日: -
- 出典: CISA KEV
- 概要: Linux Kernel contains a heap out-of-bounds write vulnerability that could allow an attacker to gain privileges or cause a DoS (via heap memory corruption) through user name space.
- 参照:
  - https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/net/netfilter/x_tables.c?id=9fa492cdc160cd27ce1046cb36f47d3b2b1efa21 ; https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/net/netfilter/x_tables.c?id=b29c457a6511435960115c0f548c4360d5f4801d ; https://security.netapp.com/advisory/ntap-20210805-0010/ ; https://github.com/google/security-research/security/advisories/GHSA-xxx5-8mvq-3528 ; https://nvd.nist.gov/vuln/detail/CVE-2021-22555

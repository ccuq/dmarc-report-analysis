# gls-france_com = "v=spf1 ip4:213.30.190.1/24 mx include:_spf.psm.knowbe4.com include:spf.9services.com include:spf.protection.outlook.com include:spf.sendinblue.com a:glsmail01.gls-group.eu a:glsmail02.gls-group.eu a:glsmail03.gls-group.eu -all"

domain_name = 'gls-france.com'

spf_record = {'gls-france.com': 'v=spf1 ip4:213.30.190.1/24 mx include:_spf.psm.knowbe4.com include:9services.com include:spf.protection.outlook.com include:spf.sendinblue.com a:glsmail01.gls-group.eu a:glsmail02.gls-group.eu a:glsmail03.gls-group.eu -all',
    'spf.protection.outlook.com': 'v=spf1 ip4:40.92.0.0/15 ip4:40.107.0.0/16 ip4:52.100.0.0/14 ip4:104.47.0.0/17 ip6:2a01:111:f400::/48 ip6:2a01:111:f403::/48 include:spfd.protection.outlook.com -all',
    'spfd.protection.outlook.com': 'v=spf1 ip4:51.4.72.0/24 ip4:51.5.72.0/24 ip4:51.5.80.0/27 ip4:51.4.80.0/27 ip6:2a01:4180:4051:0800::/64 ip6:2a01:4180:4050:0800::/64 ip6:2a01:4180:4051:0400::/64 ip6:2a01:4180:4050:0400::/64 -all',
    '9services.com': 'v=spf1 ip4:84.96.93.160/28 ip4:87.255.132.64/27 ip4:109.1.66.0/27 ip4:109.1.67.0/27 ip4:109.1.68.0/27 ip4:109.1.69.0/27 ip4:109.1.70.0/27 ip4:109.1.71.0/27 ip4:109.1.72.0/27 ip4:109.1.73.0/27 ip4:109.1.74.0/27 ip4:109.1.75.0/27 ip4:84.96.72.121 ip4:84.96.93.153 ip4:93.20.84.143 -all',
    '_spf.psm.knowbe4.com': 'v=spf1 ip4:23.21.109.197 ip4:23.21.109.212 ip4:147.160.167.14 ip4:147.160.167.15 ip4:52.49.235.189 ip4:52.49.201.246 -all',
    'spf.sendinblue.com': 'v=spf1 ip4:185.41.28.0/22 ip4:94.143.16.0/21 ip4:185.24.144.0/22 ip4:153.92.224.0/19 ip4:213.32.128.0/18 ip4:185.107.232.0/22 ip4:77.32.128.0/18 ip4:77.32.192.0/19 ip4:212.146.192.0/18 ~all',
    'glsmail01.gls-group.eu': '193.106.225.235',
    'glsmail02.gls-group.eu': '193.106.225.236',
    'glsmail03.gls-group.eu': '193.106.225.239',
    'spm04.gls-group.eu': '193.106.224.164',
    'spm01.gls-group.eu': '193.106.224.161',
    'spm03.gls-group.eu': '193.106.224.163',
    'spm02.gls-group.eu': '193.106.224.162'}

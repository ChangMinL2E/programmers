-- 코드를 입력하세요

SELECT A.APNT_NO, C.PT_NAME, C.PT_NO, A.MCDP_CD, B.DR_NAME, A.APNT_YMD
FROM APPOINTMENT A
JOIN DOCTOR B ON B.DR_ID = A.MDDR_ID
JOIN PATIENT C ON A.PT_NO = C.PT_NO
WHERE A.APNT_CNCL_YN = 'N' AND A.MCDP_CD = 'CS' AND A.APNT_YMD LIKE '2022-04-13%'
ORDER BY A.APNT_YMD;


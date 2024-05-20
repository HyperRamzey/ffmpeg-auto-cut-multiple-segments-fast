# ffmpeg-auto-cut-multiple-segments-fast
Fast ffmpeg python script that cuts out multiple segments from video based on timecodes. Uses HH:SS:MM format, example in readme.


## timecodes format
timecodes should be provided in this format: HH:MM:SS-HH:MM:SS, (start of the segment you need to cut - end of the segment)

Example:
```
00:00:00-00:11:18,00:14:28-00:15:08,00:15:25-00:15:31,00:16:26-00:17:10,00:18:07-00:18:42,00:19:18-00:19:38,00:23:30-00:23:48,00:26:56-00:27:16,00:28:53-00:29:33,00:31:49-00:32:04,00:32:10-00:32:20,00:36:25-00:36:47,00:42:11-00:42:20,00:45:45-00:46:08,00:53:22-00:53:40,00:54:33-00:54:45,01:01:09-1:01:12,01:01:19-1:01:21,01:06:48-1:07:18,01:08:12-1:08:17,01:10:48-1:10:58,01:11:07-1:11:55,01:12:05-1:12:17,01:13:39-1:13:48,01:25:25-1:25:40,01:28:33-1:28:43,01:31:31-1:42:38
```

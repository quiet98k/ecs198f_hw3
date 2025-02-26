import pytest


#Add testcases Here

def test_basic():
    from foo_bar_baz import foo_bar_baz

    assert False != True
    assert foo_bar_baz(1) == "1"
    assert foo_bar_baz(2) == "1 2"
    assert foo_bar_baz(3) == "1 2 Foo"
    assert foo_bar_baz(4) == "1 2 Foo 4"
    assert foo_bar_baz(5) == "1 2 Foo 4 Bar"
    assert foo_bar_baz(6) == "1 2 Foo 4 Bar Foo"
    assert foo_bar_baz(7) == "1 2 Foo 4 Bar Foo 7"
    
    assert foo_bar_baz(15) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz"

    assert foo_bar_baz(0) == ""
    assert foo_bar_baz(-5) == ""

    assert foo_bar_baz(30) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz 16 17 Foo 19 Bar Foo 22 23 Foo Bar 26 Foo 28 29 Baz" 
    assert foo_bar_baz(1000) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz 16 17 Foo 19 Bar Foo 22 23 Foo Bar 26 Foo 28 29 Baz 31 32 Foo 34 Bar Foo 37 38 Foo Bar 41 Foo 43 44 Baz 46 47 Foo 49 Bar Foo 52 53 Foo Bar 56 Foo 58 59 Baz 61 62 Foo 64 Bar Foo 67 68 Foo Bar 71 Foo 73 74 Baz 76 77 Foo 79 Bar Foo 82 83 Foo Bar 86 Foo 88 89 Baz 91 92 Foo 94 Bar Foo 97 98 Foo Bar 101 Foo 103 104 Baz 106 107 Foo 109 Bar Foo 112 113 Foo Bar 116 Foo 118 119 Baz 121 122 Foo 124 Bar Foo 127 128 Foo Bar 131 Foo 133 134 Baz 136 137 Foo 139 Bar Foo 142 143 Foo Bar 146 Foo 148 149 Baz 151 152 Foo 154 Bar Foo 157 158 Foo Bar 161 Foo 163 164 Baz 166 167 Foo 169 Bar Foo 172 173 Foo Bar 176 Foo 178 179 Baz 181 182 Foo 184 Bar Foo 187 188 Foo Bar 191 Foo 193 194 Baz 196 197 Foo 199 Bar Foo 202 203 Foo Bar 206 Foo 208 209 Baz 211 212 Foo 214 Bar Foo 217 218 Foo Bar 221 Foo 223 224 Baz 226 227 Foo 229 Bar Foo 232 233 Foo Bar 236 Foo 238 239 Baz 241 242 Foo 244 Bar Foo 247 248 Foo Bar 251 Foo 253 254 Baz 256 257 Foo 259 Bar Foo 262 263 Foo Bar 266 Foo 268 269 Baz 271 272 Foo 274 Bar Foo 277 278 Foo Bar 281 Foo 283 284 Baz 286 287 Foo 289 Bar Foo 292 293 Foo Bar 296 Foo 298 299 Baz 301 302 Foo 304 Bar Foo 307 308 Foo Bar 311 Foo 313 314 Baz 316 317 Foo 319 Bar Foo 322 323 Foo Bar 326 Foo 328 329 Baz 331 332 Foo 334 Bar Foo 337 338 Foo Bar 341 Foo 343 344 Baz 346 347 Foo 349 Bar Foo 352 353 Foo Bar 356 Foo 358 359 Baz 361 362 Foo 364 Bar Foo 367 368 Foo Bar 371 Foo 373 374 Baz 376 377 Foo 379 Bar Foo 382 383 Foo Bar 386 Foo 388 389 Baz 391 392 Foo 394 Bar Foo 397 398 Foo Bar 401 Foo 403 404 Baz 406 407 Foo 409 Bar Foo 412 413 Foo Bar 416 Foo 418 419 Baz 421 422 Foo 424 Bar Foo 427 428 Foo Bar 431 Foo 433 434 Baz 436 437 Foo 439 Bar Foo 442 443 Foo Bar 446 Foo 448 449 Baz 451 452 Foo 454 Bar Foo 457 458 Foo Bar 461 Foo 463 464 Baz 466 467 Foo 469 Bar Foo 472 473 Foo Bar 476 Foo 478 479 Baz 481 482 Foo 484 Bar Foo 487 488 Foo Bar 491 Foo 493 494 Baz 496 497 Foo 499 Bar Foo 502 503 Foo Bar 506 Foo 508 509 Baz 511 512 Foo 514 Bar Foo 517 518 Foo Bar 521 Foo 523 524 Baz 526 527 Foo 529 Bar Foo 532 533 Foo Bar 536 Foo 538 539 Baz 541 542 Foo 544 Bar Foo 547 548 Foo Bar 551 Foo 553 554 Baz 556 557 Foo 559 Bar Foo 562 563 Foo Bar 566 Foo 568 569 Baz 571 572 Foo 574 Bar Foo 577 578 Foo Bar 581 Foo 583 584 Baz 586 587 Foo 589 Bar Foo 592 593 Foo Bar 596 Foo 598 599 Baz 601 602 Foo 604 Bar Foo 607 608 Foo Bar 611 Foo 613 614 Baz 616 617 Foo 619 Bar Foo 622 623 Foo Bar 626 Foo 628 629 Baz 631 632 Foo 634 Bar Foo 637 638 Foo Bar 641 Foo 643 644 Baz 646 647 Foo 649 Bar Foo 652 653 Foo Bar 656 Foo 658 659 Baz 661 662 Foo 664 Bar Foo 667 668 Foo Bar 671 Foo 673 674 Baz 676 677 Foo 679 Bar Foo 682 683 Foo Bar 686 Foo 688 689 Baz 691 692 Foo 694 Bar Foo 697 698 Foo Bar 701 Foo 703 704 Baz 706 707 Foo 709 Bar Foo 712 713 Foo Bar 716 Foo 718 719 Baz 721 722 Foo 724 Bar Foo 727 728 Foo Bar 731 Foo 733 734 Baz 736 737 Foo 739 Bar Foo 742 743 Foo Bar 746 Foo 748 749 Baz 751 752 Foo 754 Bar Foo 757 758 Foo Bar 761 Foo 763 764 Baz 766 767 Foo 769 Bar Foo 772 773 Foo Bar 776 Foo 778 779 Baz 781 782 Foo 784 Bar Foo 787 788 Foo Bar 791 Foo 793 794 Baz 796 797 Foo 799 Bar Foo 802 803 Foo Bar 806 Foo 808 809 Baz 811 812 Foo 814 Bar Foo 817 818 Foo Bar 821 Foo 823 824 Baz 826 827 Foo 829 Bar Foo 832 833 Foo Bar 836 Foo 838 839 Baz 841 842 Foo 844 Bar Foo 847 848 Foo Bar 851 Foo 853 854 Baz 856 857 Foo 859 Bar Foo 862 863 Foo Bar 866 Foo 868 869 Baz 871 872 Foo 874 Bar Foo 877 878 Foo Bar 881 Foo 883 884 Baz 886 887 Foo 889 Bar Foo 892 893 Foo Bar 896 Foo 898 899 Baz 901 902 Foo 904 Bar Foo 907 908 Foo Bar 911 Foo 913 914 Baz 916 917 Foo 919 Bar Foo 922 923 Foo Bar 926 Foo 928 929 Baz 931 932 Foo 934 Bar Foo 937 938 Foo Bar 941 Foo 943 944 Baz 946 947 Foo 949 Bar Foo 952 953 Foo Bar 956 Foo 958 959 Baz 961 962 Foo 964 Bar Foo 967 968 Foo Bar 971 Foo 973 974 Baz 976 977 Foo 979 Bar Foo 982 983 Foo Bar 986 Foo 988 989 Baz 991 992 Foo 994 Bar Foo 997 998 Foo Bar"


    assert foo_bar_baz(6).count(" ") == 5

    with pytest.raises(TypeError):
        foo_bar_baz("10")
    with pytest.raises(TypeError):
        foo_bar_baz(10.5)
    with pytest.raises(TypeError):
        foo_bar_baz([10])
    with pytest.raises(TypeError):
        foo_bar_baz(None)
    with pytest.raises(TypeError):
        foo_bar_baz()
        
    assert foo_bar_baz(3) == "1 2 Foo"
    assert foo_bar_baz(5) == "1 2 Foo 4 Bar"
    assert foo_bar_baz(6) == "1 2 Foo 4 Bar Foo"
    assert foo_bar_baz(10) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar"


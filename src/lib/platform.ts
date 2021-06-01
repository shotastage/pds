
const Platform = {
    macOS: 'macOS',
    Linux: 'linux',
    Windows: 'NT',
    Unkown: 'Unkown'
} as const;

type Platform = typeof Platform[keyof typeof Platform];

const platform = (): Platform => {
    switch (process.platform) {
        case 'darwin':
            return Platform.macOS;
        case 'linux':
            return Platform.Linux;
        case 'win32' || "cygwin":
            return Platform.Windows;
    }

    return Platform.Unkown;
};
